import { defineConfig } from "@playwright/test";

/** Set PLAYWRIGHT_E2E=0 to skip browser E2E; BASE_URL targets live server (default localhost:8090). */
export default defineConfig({
  testDir: ".",
  testMatch: "*.spec.ts",
  timeout: 120_000,
  expect: { timeout: 10_000 },
  retries: 0,
  workers: 1,
  reporter: [["html", { open: "never" }], ["list"]],
  use: {
    baseURL: process.env.BASE_URL || "http://localhost:8090",
    screenshot: "only-on-failure",
    trace: "retain-on-failure",
    headless: true,
  },
  projects: [{ name: "chromium", use: { browserName: "chromium" } }],
});
