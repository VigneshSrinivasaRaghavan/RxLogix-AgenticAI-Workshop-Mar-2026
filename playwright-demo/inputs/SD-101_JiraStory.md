# SD-101 — [E2E] Complete Order Flow: Login to Order Confirmation on Sauce Demo

## Story Details

| Field       | Value                                      |
|-------------|--------------------------------------------|
| Story ID    | SD-101                                     |
| Story Type  | Test / QA Automation                       |
| Priority    | High                                       |
| Labels      | `e2e`, `regression`, `migration`, `playwright` |
| Component   | Web — SauceDemo                            |
| Fix Version | v1.0                                       |

---

## User Story

> As a **registered user**,
> I want to **log in, add products to my cart, and complete a purchase**,
> So that **I can verify the end-to-end order flow works correctly on the Sauce Demo application.**

---

## Background / Context

The Sauce Demo application (`https://www.saucedemo.com/`) is the target AUT (Application Under Test)
for validating the complete shopping flow. This story covers the critical path from login through to
order confirmation. This test is being migrated from the existing UFT Keyword-Driven framework to
Playwright with Page Object Model.

---

## Acceptance Criteria

```
AC-1: LOGIN
  Given the user navigates to https://www.saucedemo.com/
  When the user enters username "standard_user" and password "secret_sauce"
  And clicks the Login button
  Then the user should be redirected to the Products page

AC-2: ADD ITEMS TO CART
  Given the user is on the Products page
  When the user clicks "Add to cart" on the "Sauce Labs Backpack" tile
  And clicks "Add to cart" on the "Sauce Labs Bike Light" tile
  And clicks the Shopping Cart icon
  Then the user should be redirected to the Your Cart page
  And both selected items should be visible in the cart

AC-3: PROCEED TO CHECKOUT
  Given the user is on the Your Cart page
  When the user clicks the "Checkout" button
  Then the user should be redirected to the Checkout: Your Information page

AC-4: FILL CHECKOUT INFORMATION
  Given the user is on the Checkout: Your Information page
  When the user enters a valid First Name
  And enters a valid Last Name
  And enters a valid Zip/Postal Code
  And clicks the "Continue" button
  Then the user should be redirected to the Checkout: Overview page

AC-5: COMPLETE THE ORDER
  Given the user is on the Checkout: Overview page
  When the user clicks the "Finish" button
  Then the user should be redirected to the Checkout: Complete page
  And the text "Thank you for your order!" should be visible on the page
```

---

## Test Data

| Field           | Value                          |
|-----------------|--------------------------------|
| Username        | `standard_user`                |
| Password        | `secret_sauce`                 |
| First Name      | Random (generated at runtime)  |
| Last Name       | Random (generated at runtime)  |
| Zip/Postal Code | Random (generated at runtime)  |

---

## Out of Scope

- Login with invalid credentials
- Removing items from cart
- Applying promo codes
- Payment gateway validation

---

## Notes for Automation Agent

- Prefer `data-test` attributes for all element locators
- Screenshots required at each major step
- Refer to the UFT Keyword-Driven Excel (`SauceDemo_UFT_KeywordDriven.xlsx`) for the exact step-by-step flow and element references
- **Excel takes priority over this story in case of any conflict**
