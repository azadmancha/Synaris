"use client";

import { useState } from "react";
import { fetchJson } from "../lib/api";

export function useUserSync() {
  const [syncResult, setSyncResult] = useState<string | null>(null);
  const [isSyncing, setIsSyncing] = useState(false);

  async function syncProfile() {
    setSyncResult(null);
    setIsSyncing(true);

    try {
      const user = await fetchJson<{ email: string }>("/users/sync", {
        method: "POST",
      });
      setSyncResult(`Synced profile: ${user.email}`);
    } catch (error) {
      setSyncResult(error instanceof Error ? error.message : "Sync failed.");
    } finally {
      setIsSyncing(false);
    }
  }

  return { syncResult, isSyncing, syncProfile };
}
