import { NextResponse } from 'next/server';
import { issueSession, readConfig, RequestBudget, SessionError } from '../../../features/session/server/session';

export const runtime = 'nodejs';
export const dynamic = 'force-dynamic';
const budget = new RequestBudget();
const headers = { 'Cache-Control': 'no-store, private' };

export async function POST(request: Request) {
  if (!budget.consume()) {
    return NextResponse.json({ error: 'Too many session requests. Wait a minute and try again.' }, {
      status: 429, headers: { ...headers, 'Retry-After': '60' },
    });
  }
  try {
    return NextResponse.json(await issueSession(request, readConfig()), { headers });
  } catch (error) {
    if (error instanceof SessionError) {
      return NextResponse.json({ error: error.message }, { status: error.status, headers });
    }
    // Never return SDK errors or environment values to the browser.
    return NextResponse.json({ error: 'The voice session could not be started. Check the server configuration.' }, { status: 503, headers });
  }
}
