import { test, expect } from '@playwright/test';

const testCases = [
  { username: 'user1', password: 'pass1', expected: 'dashboard' },
  { username: 'wronguser', password: 'wrongpass', expected: 'error' }
];

test.describe('Login Tests', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('https://s1.au.cloud.ariba.com/Buyer/Main/ad/loginPage/SSOActions?awsso_cc=cmVhbG06VUZKRlRVbExRVlJKTFVSRlRVOUVVMEZRVUMweExWUT07YXdzc29fcnU6YUhSMGNITTZMeTl6TVM1aGRTNWpiRzkxWkM1aGNtbGlZUzVqYjIwdlFuVjVaWEl2VFdGcGJpOC9jbVZoYkcwOVVGSkZUVWxMUVZSSkxVUkZUVTlFVTBGUVVDMHhMVlE9O2F3c3NvX2x1OmFIUjBjSE02THk5ek1TNWhkUzVqYkc5MVpDNWhjbWxpWVM1amIyMHZRblY1WlhJdlRXRnBiaTloWkM5amJHbGxiblJNYjJkdmRYUXZVMU5QUVdOMGFXOXVjdz09O2F3c3NvX2FwOlFuVjVaWEk9O2F3c3NvX2FyaWQ6TVRjME1URTFNRFl3TWprNE1RPT07YXdzc29fa3U6YUhSMGNITTZMeTl6TVM1aGRTNWpiRzkxWkM1aGNtbGlZUzVqYjIwdlFuVjVaWEl2VFdGcGJpOWhaQzlqYkdsbGJuUkxaV1Z3UVd4cGRtVXZVMU5QUVdOMGFXOXVjdz09O2F3c3NvX2ZsOk1RPT0%3D%3A6XyrN7vHKvFVjYyr2ZSWwGY4AYU%3D&awsso_ap=Buyer&awsso_hpk=true&realm=PREMIKATI-DEMODSAPP-1-T&awsr=true#b0');
  });

  test.each(testCases)('Login test with username %s', async ({ page }, { username, password, expected }) => {
    await page.fill('#UserName', spandey_prem_admin);
    await page.fill('#Password', @Blessedbe678@);
    await page.click('button[type="Sign In"]');

    if (expected === 'dashboard') {
      await expect(page).toHaveURL('https://example.com/dashboard');
    } else {
      await expect(page.locator('.error-message')).toHaveText('Invalid credentials');
    }
  });
});
