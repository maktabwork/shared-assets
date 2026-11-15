FINDINGS = """Audit of the prescription upload screen (Noor Pharmacy app, Android, Chrome DevTools at 360px):
1. Upload button text contrast is 2.8:1 (needs 4.5:1). High.
2. Camera permission is requested before any explanation of why. High.
3. Failed upload shows "Error 4012" with no way to retry. High.
4. No progress shown for 12 seconds during upload. Medium.
5. Arabic button label is clipped at 360px width. Medium.
6. Remove-photo icon is 32px, below the 44px tap size. Medium.
7. No success screen after upload; user lands back on the same screen. Low.
8. Cancel discards the photo without asking. Low.
Not checked: iPhone/Safari, logged-in order history, the camera flow on a real device."""

TASKS = [
 dict(id="t1", title="Mo tells the AM what it understood on a new ticket", lang="en",
  prompt="""You just finished the understanding step on ticket 214. Material:
Ticket: "Refresh the prescription upload screen" for Noor Pharmacy. Customers say it is confusing. Client wants (a) a review of the current upload screen, (b) better error texts, (c) a clearer "My orders" menu. Link: https://noor-pharmacy.example/app. Client context: Arabic first, calm tone, brand blue. The ticket does not say whether uploading by camera is in scope or only picking a file from the phone.
Write the message you show the AM now. Per the method, you wait for their OK before building.""",
  facts=[r"\b(audit|review)\b", r"error text|texts|wording", r"my orders|menu|navigation", r"camera", r"\bok\b|confirm|approv|go ahead|green light"]),
 dict(id="t2", title="Step summary posted to the ticket (finish_work summary)", lang="en",
  prompt=FINDINGS+"\n\nWrite the `summary` for finish_work: what was done and the main findings (it appears on the ticket for the AM and reviewers).",
  facts=[r"\b(8|eight)\b", r"2\.8", r"camera", r"4012|error", r"iphone|safari|ios", r"progress|12 ?s"]),
 dict(id="t3", title="Mo reports a blocker to the AM", lang="en",
  prompt="""start_work(ticket_id=388) returned: "No such ticket for this key. Use a key made for one client." You have not done anything on the ticket. The plugin probably holds another client's key. The fix is `/plugin configure mo@monjizeen` and pasting the right client's key. Tell the AM.""",
  facts=[r"\bkey\b", r"/plugin configure|configure", r"another client|other client|different client|wrong client", r"(didn't|did not|haven't|have not|nothing|stopp|not done|no work)"]),
 dict(id="t4", title="Top box of the audit page, read by the client", lang="en",
  prompt=FINDINGS+"\n\nWrite the text for the top box of the HTML page the client (a pharmacy owner, not technical) will read first. The page's detail follows below.",
  facts=[r"\b(8|eight)\b", r"button", r"camera", r"error|retry|try again", r"iphone|safari|ios|not (yet )?(checked|tested)", r"high|first|priorit|most important|urgent"]),
 dict(id="t5", title="Background Mo final report to the AM", lang="en",
  prompt="""You ran ticket 214 in the background. Done: understanding step (step 51), UX audit (step 52, 8 findings, 3 high), error texts (step 53, 14 strings, Arabic and English). Saved to the client's Seyaq: "tone: calm, no exclamation marks". Open question: is the app Android only, or also iPhone? Ticket link: https://app.monjizeen.com/tickets/214. Write your end report to the AM.""",
  facts=[r"tickets/214", r"\b51\b|understanding", r"\b52\b|audit", r"\b53\b|error texts|texts|strings", r"exclamation|tone|calm", r"iphone|ios|android"]),
 dict(id="t6", title="Unclear ticket, asks the AM (Arabic)", lang="ar",
  prompt="""التذكرة 301 نصها كاملاً: "حسّنوا التطبيق". لا يوجد رابط ولا شاشة محددة ولا موعد. اكتب للمسؤول عن الحساب (AM) بالعربية ما تحتاجه منه قبل أن تبدأ: أي شاشة، وما الهدف، وما الموعد.""",
  facts=[r"الشاشة|شاشة", r"الهدف|هدف", r"الموعد|موعد|تاريخ"]),
]
JARGON = r"\b(leverage|utili[sz]e|robust|comprehensive|holistic|synerg\w*|stakeholders?|paradigm|endpoints?|payloads?|heuristics?|affordances?|a11y|wcag|contrast ratio|touch targets?|tap targets?|friction|granular|seamless|streamline|actionable|deliverables?|workflows?|methodolog\w*|ux|ui|cta|viewport|modal|state management|onboarding|iterat\w*|bandwidth|alignment|scope creep|best practices?)\b"
FILLER = r"(i'd be happy|i would be happy|happy to|great question|certainly|of course|in order to|it'?s important to note|it is important to note|please note|let me know if|feel free|i hope this|here is a summary|here's a summary|here'?s what|i will now|i'll now|as requested|in summary|in conclusion|to summarize|overall,|essentially|basically|might want to consider|it seems|عن طريق|يسعدني|بكل سرور|آمل أن|لا تتردد|في الختام|ملخصاً)"
