import { test, expect } from "@playwright/test";

const LANGUAGES = ["en", "fr"];

test.describe("Language switching (EN/FR)", () => {
  for (const lang of LANGUAGES) {
    test(`loads in ${lang}`, async ({ page, context }) => {
      const baseURL = process.env.BASE_URL || "http://localhost:8090";
      await context.addCookies([
        { name: "sf_lang", value: lang, url: baseURL },
      ]);
      await page.goto("/");
      expect(await page.title()).toBeTruthy();
      const content = await page.textContent("body");
      expect(content!.length).toBeGreaterThan(100);
    });
  }

  test("locale API returns translations", async ({ request }) => {
    for (const lang of LANGUAGES) {
      const response = await request.get(`/api/i18n/${lang}.json`);
      expect(response.status()).toBe(200);
      const data = await response.json();
      expect(Object.keys(data).length).toBeGreaterThan(10);
    }
  });

  test("unsupported locale falls back to English catalog", async ({
    request,
  }) => {
    const zh = await request.get("/api/i18n/zh.json").then((r) => r.json());
    const en = await request.get("/api/i18n/en.json").then((r) => r.json());
    expect(zh.nav_portfolio).toBe(en.nav_portfolio);
  });
});
