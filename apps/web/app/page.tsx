"use client";

import { useSession, signIn, signOut } from "next-auth/react";
import { useUserSync } from "../hooks/useUserSync";

export default function HomePage() {
  const { data: session, status } = useSession();
  const { syncResult, isSyncing, syncProfile } = useUserSync();

  return (
    <main className="min-h-screen bg-slate-950 text-slate-100">
      <div className="mx-auto flex min-h-screen max-w-5xl flex-col px-6 py-16">
        <header className="mb-12">
          <p className="text-sm uppercase tracking-[0.3em] text-slate-400">Synaris</p>
          <h1 className="mt-4 text-4xl font-semibold text-white sm:text-5xl">A secure AI learning foundation.</h1>
          <p className="mt-4 max-w-2xl text-slate-300">
            Start with modern authentication, a production-ready API, and an extensible frontend built for future AI-powered learning.
          </p>
        </header>

        <section className="space-y-6 rounded-3xl border border-slate-800 bg-slate-900/90 p-8 shadow-xl shadow-slate-950/20">
          <div>
            <h2 className="text-2xl font-semibold text-white">Authentication</h2>
            <p className="mt-2 text-slate-400">
              Google sign-in is powered by Auth.js and integrated into Synaris with a reusable session flow.
            </p>
          </div>

          {status === "loading" ? (
            <div className="rounded-2xl bg-slate-800 p-6">Loading session...</div>
          ) : session?.user ? (
            <div className="space-y-4 rounded-2xl border border-slate-800 bg-slate-950/80 p-6">
              <p className="text-slate-300">Signed in as {session.user.email}</p>
              <div className="flex flex-wrap gap-3">
                <button onClick={() => void syncProfile()} disabled={isSyncing} className="rounded-full bg-brand-700 px-5 py-3 font-semibold text-white transition hover:bg-brand-500 disabled:cursor-not-allowed disabled:opacity-70">
                  {isSyncing ? "Syncing profile..." : "Sync profile with backend"}
                </button>
                <button onClick={() => void signOut()} className="rounded-full border border-slate-700 px-5 py-3 font-semibold text-slate-100 transition hover:bg-slate-800">
                  Sign out
                </button>
              </div>
              {syncResult ? <p className="text-sm text-slate-300">{syncResult}</p> : null}
            </div>
          ) : (
            <div className="rounded-2xl border border-slate-800 bg-slate-950/80 p-6">
              <p className="text-slate-300">No active session detected.</p>
              <button onClick={() => void signIn("google")} className="mt-4 rounded-full bg-brand-700 px-5 py-3 font-semibold text-white transition hover:bg-brand-500">
                Sign in with Google
              </button>
            </div>
          )}
        </section>
      </div>
    </main>
  );
}
