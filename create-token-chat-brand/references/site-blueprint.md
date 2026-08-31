# Fixed site blueprint

Use this sitemap and section order for every brand. Do not add, remove, merge, or rename pages unless the user explicitly changes the template.

## Shared shell

Header:

- primary logo linked to the homepage
- Chat
- Pricing
- FAQ
- Log in
- Register
- My account state when authenticated
- Cart

Footer:

- logo
- short brand description
- support/contact link
- Privacy policy, Refund policy, Terms and conditions, and Cookies policy link labels only
- copyright line
- implementation-supplied company and payment fields, if any

Cookie component:

- a short neutral notice
- Accept and Decline control labels
- policy link label

Do not write policy bodies, legal assertions, or consent logic.

## Homepage `/`

Keep this order:

1. Hero: eyebrow if useful, H1, theme descriptor, primary CTA to Chat, hero image.
2. Intro: one compact paragraph explaining the product and conversational value.
3. Benefits: heading plus exactly four theme-specific benefit items with four matching icons.
4. Registration CTA: short bridge copy and CTA to Register.
5. Testimonials: heading plus exactly three customer-supplied quote slots and name/role fields. Write the section framing, not the quotes.

## Chat `/chat/`

1. H1 addressing what the user can ask or achieve.
2. Short explanation of the chat's role and useful inputs.
3. Exactly three `How it works` steps.
4. Qualitative token note with no quantities, prices, rates, or allowances.
5. Chat heading, empty-state greeting, input placeholder, send label, and four starter prompts.
6. Loading, retry, refusal, connection, sign-in, insufficient-balance, and session-expired states.

Create `content/chat-persona.md` with:

- role and purpose
- allowed topics and capabilities
- response style
- first-turn onboarding behavior
- safety and escalation boundaries
- uncertainty behavior
- privacy-aware handling of sensitive inputs
- refusal style
- eight representative user prompts with expected response characteristics

Do not include secrets, model configuration values, or claims that the product stores or encrypts data unless verified separately.

## Pricing `/pricing/`

1. Page heading and short introduction.
2. Exactly three token-package cards using theme-appropriate, non-numeric tier names.
3. Each card gets a short description and purchase CTA.
4. Pay-as-you-go heading, explanation, amount-field label, balance-preview label, validation state, and add-to-cart CTA.

Do not supply token amounts, prices, exchange rates, savings, free allocations, usage cost, or expiry. Do not place text or numbers in package artwork.

## FAQ `/faq/`

Write answers for exactly these ten question intents, phrased in the brand voice:

1. What the service is and what it offers.
2. How the themed chat works.
3. How tokens work at a qualitative level.
4. How user information is handled, without inventing controls or guarantees.
5. What the chat can help users do.
6. What happens when a balance is insufficient.
7. What makes the experience distinct.
8. How users obtain support.
9. Who benefits most.
10. Whether the experience suits beginners.

## Authentication and account

`/login/`:

- heading, field labels, password visibility label, remember-me label, submit label, registration link, password-recovery link, and error states

`/register/`:

- heading, username/email/password labels, password guidance, terms-acceptance label with an implementation-supplied URL, submit label, login link, and validation states

`/lostpassword/`:

- heading, instructions, username/email label, submit label, confirmation state, and failure state

`/my-account/`:

- greeting, token-balance label, buy-tokens CTA, profile labels, order-history labels, password controls, logout label, and empty states

## Commerce

`/cart/`:

- cart heading, line-item labels, quantity/remove labels, totals labels without values, checkout CTA, continue-shopping CTA, and empty-cart state

`/checkout/`:

- heading, account/billing field labels, order-summary labels, payment-section heading, consent-control label, submit-order CTA, validation states, processing state, success state, and failure state

Do not state payment-method availability or security claims. Payment-provider marks and required compliance text come from implementation.

## Contact `/contact/`

- heading and one short support paragraph
- name, email, subject, and message labels
- privacy acceptance label with an implementation-supplied policy URL
- submit label
- success, validation, and failure states

## Transactional messages

Create subject line, preview text, body, and CTA copy for:

- welcome/account created
- email verification when applicable
- password reset
- password changed
- token purchase receipt without values
- low balance
- purchase failed
- support request received

Do not invent prices, order values, company addresses, response-time promises, or legal language.
