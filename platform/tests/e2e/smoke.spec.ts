import { test, expect } from "@playwright/test";

/**
 * Minimal CI smoke — login page + health API only.
 * Full suite: npm test (see LOCAL-DEV.md).
 */

test.describe("Smoke", () => {
  test("login page loads", async ({ page }) => {
    await page.goto("/login", { waitUntil: "domcontentloaded" });
    await expect(page).toHaveTitle(/Architekt|Login/i);
    await expect(page.locator("#loginForm")).toBeVisible();
    await expect(page.locator('input[type="email"], #email')).toBeVisible();
  });

  test("GET /api/health returns ok", async ({ request }) => {
    const r = await request.get("/api/health");
    expect(r.status()).toBe(200);
    const data = await r.json();
    expect(data.status).toBe("ok");
  });
});
