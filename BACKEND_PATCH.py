"""
BACKEND PATCH — cheptiony.com new pages
========================================
Replace the existing CLIENT AUTO-REPLY SWITCH block in your
capture_lead() function with the expanded version below.

The original code had two conditions:
  1. "contact" in source  → standard reply
  2. else                 → StratBot roadmap reply  (Techtube)

New sources added by the cheptiony.com rebuild:
  - "consulting-homepage"  → consulting inquiry auto-reply
  - "renewed-mind-guide"   → download confirmation + PDF link
  - "book-waitlist"        → waitlist confirmation + early chapter promise

HOW TO APPLY:
  Find this block in your existing code:
    # 2. CLIENT AUTO-REPLY SWITCH
  Replace everything from that comment down to (but not including)
  the closing return statement with the code below.
  
  ⚠️  Update PDF_DOWNLOAD_URL with your actual Firebase Hosting URL
      once you confirm the exact PDF filename in your public folder.
"""

# ── Configuration ──────────────────────────────────────────────────────────
PDF_DOWNLOAD_URL = "https://cheptiony.com/renewed-mind-guide.pdf"
# ↑ Confirm this filename matches what you pushed to your public/ folder.
#   If the file is named differently, update this constant.

DONATION_LINK = "https://paypal.me/YOUR_PAYPAL"
# ↑ Replace with your actual PayPal.me URL or remove the donation line below.


# ── Drop-in replacement for the CLIENT AUTO-REPLY SWITCH block ─────────────

        # 2. CLIENT AUTO-REPLY SWITCH
        # Checks source to decide which email template to send the client.

        source_lower = lead.source.lower()

        if "contact" in source_lower:
            # ── Standard contact page reply ──────────────────────────────
            client_subject = f"Got it: {lead.topic}"
            client_body = (
                f"Dear {lead.name},\n\n"
                f"Thank you for reaching out regarding '{lead.topic}'. "
                f"I've received your message and will get back to you within 24 hours.\n\n"
                f"In the meantime, feel free to browse the Insights section on the site "
                f"or connect with me on WhatsApp: +254 712 828 453\n\n"
                f"Best regards,\nCheptiony Mutai\ncheptiony.com"
            )

        elif "consulting" in source_lower:
            # ── Consulting inquiry reply ──────────────────────────────────
            client_subject = f"Consulting Request Received — {lead.topic}"
            client_body = (
                f"Dear {lead.name},\n\n"
                f"Thank you for your consulting inquiry about '{lead.topic}'. "
                f"I've reviewed your message and will be in touch within 24 hours "
                f"to discuss next steps.\n\n"
                f"If you'd like to speak sooner, you can reach me directly on "
                f"WhatsApp: +254 712 828 453\n\n"
                f"Looking forward to connecting,\n"
                f"Cheptiony Mutai\nStrategic Media Consultant\ncheptiony.com"
            )

        elif "renewed-mind" in source_lower:
            # ── Renewed Mind guide download email ─────────────────────────
            client_subject = "Your Free Guide: Renewed Mind, Abundant Life"
            client_body = (
                f"Dear {lead.name},\n\n"
                f"Thank you for requesting the Renewed Mind, Abundant Life guide. "
                f"Here is your personal download link:\n\n"
                f"👉  {PDF_DOWNLOAD_URL}\n\n"
                f"This 40-day journey was written to help you rewire your mindset "
                f"for Divine Prosperity, Wisdom, and Peace. Take it one day at a time — "
                f"there's no rush.\n\n"
                f'"Do not conform to the pattern of this world, but be transformed '
                f'by the renewing of your mind." — Romans 12:2\n\n'
                f"If this guide blesses you, consider supporting Reflection Friday "
                f"with even $1 — it helps keep the teaching going every week:\n"
                f"👉  {DONATION_LINK}\n\n"
                f"God bless you,\n"
                f"Cheptiony Mutai\n"
                f"cheptiony.com | Reflection Friday on YouTube"
            )

        elif "book-waitlist" in source_lower:
            # ── Book waitlist confirmation ────────────────────────────────
            client_subject = "You're on the List — From Freelance to Fortune"
            client_body = (
                f"Dear {lead.name},\n\n"
                f"You're officially on the waitlist for From Freelance to Fortune.\n\n"
                f"Here's what happens next:\n"
                f"  • You'll be the first to know the moment pre-orders open.\n"
                f"  • Waitlist members get early chapter access before the public launch.\n"
                f"  • Waitlist members receive a launch-day discount.\n\n"
                f"This book is everything I wish I had when I started in 2009. "
                f"I'll make sure it's worth the wait.\n\n"
                f"Talk soon,\n"
                f"Cheptiony Mutai\ncheptiony.com"
            )

        else:
            # ── Fallback: StratBot / Techtube roadmap reply ───────────────
            # Catches all other sources, including StratBot submissions.
            client_subject = "Your 30-Day Video Production Roadmap"
            client_body = (
                f"Dear {lead.name},\n\n"
                f"Thank you for choosing Techtube Studio. "
                f"Here is your requested production roadmap summary:\n\n"
                f"{lead.message}\n\n"
                f"Our team is reviewing your details and will follow up shortly.\n\n"
                f"Best regards,\nTechtube Team\ntechtubestudio.com"
            )

        client_msg = MessageSchema(
            subject=client_subject,
            recipients=[lead.email],
            body=client_body,
            subtype="plain"
        )
        background_tasks.add_task(fm.send_message, client_msg)
