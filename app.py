
import re
import streamlit as st
from openai import OpenAI

# ==========================================
# GOLDEN COMPANION - HYBRID AI CHATBOT
# Water Rocket Challenge 2026
# ==========================================

st.set_page_config(
    page_title="Golden Companion | Golden Voyager",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="expanded"
)

ROCKET_NAME = "Golden Voyager"
BOT_NAME = "Golden Companion"

# ==========================================
# 1. ROCKET INFORMATION
# ==========================================

rocket_info = {
    "name": "Golden Voyager",
    "chatbot": "Golden Companion",
    "bottle": "1.5-liter Mountain Dew soda bottle",
    "length": "50 centimeters",
    "distance": "41.8 meters",
    "angle": "45 degrees",
    "fin_shape": "Tapered trapezoid",
    "fin_material": "Reused cardboard plate",
    "nose_material": "Plastic document folder sheets",
    "attachment": "Duct tape"
}

# ==========================================
# 2. COMPLETE PROTOTYPE EXPLANATIONS
# ==========================================

prototype1 = """PROTOTYPE 1

Our first prototype used a 1.5-liter soda bottle and had a short, blunt, elliptical nose cone.

BENEFITS:
We selected the bottle to balance capacity and weight. It provided space for water and compressed air without making the rocket unnecessarily heavy.

The short, blunt nose was intended to be suitable for subsonic flight.

DRAWBACKS:
The rocket had a rough overall design. The nose cone was asymmetrical and not properly aerodynamic.

The fins were not evenly attached. Some fins fell off and had to be re-glued.

These problems encouraged us to develop Prototype 2."""

prototype2 = """PROTOTYPE 2

Our second prototype was designed to be sturdier and more aerodynamic than the first.

IMPROVEMENTS:
We made the nose cone longer and smoother. We used tape instead of glue to secure the fins.

The longer nose cone helped move the rocket's center of mass forward, which can improve stability.

We filled the bottle with a little over one-third of its total volume with water.

BENEFITS:
Prototype 2 performed significantly better during testing. It traveled farther than many other teams' rockets.

DRAWBACKS:
The rocket was 55 centimeters long. This exceeded the maximum permitted length of 50 centimeters by 5 centimeters.

Because Prototype 2 performed well, we used it as the basis for our final design."""

final_model = """FINAL MODEL - GOLDEN VOYAGER

Our final rocket was based on Prototype 2, with improvements to meet the project requirements.

DESIGN:
We reduced the rocket's length from 55 centimeters to exactly 50 centimeters.

We kept the 1.5-liter Mountain Dew soda bottle.

The nose cone was made from plastic document folder sheets.

The fins were made thinner using sturdy cardboard from a reused cardboard plate.

We measured the fin placement more carefully and secured the components using duct tape.

BENEFITS:
The final rocket met the 50-centimeter length requirement.

We reused a soda bottle and a cardboard plate to reduce material waste.

These materials are affordable and widely available, making our design achievable and easy to recreate.

This demonstrates environmental sustainability and reproducibility.

The Golden Voyager successfully traveled 41.8 meters during testing.

DRAWBACKS:
The fins may not have been perfectly symmetrical due to a possible measurement error.

This could have affected the rocket's stability and flight distance.

Overall, our final rocket was successful, and we identified improvements for future designs."""

# ==========================================
# 3. QUESTIONS AND ANSWERS
# ==========================================

categories = {
    "1. General Rocket Information": {
        "What is your rocket's name?":
            "Our rocket is called the Golden Voyager!",
        "What is your chatbot's name?":
            "I'm Golden Companion, your virtual guide to the Golden Voyager!",
        "What was the goal of your project?":
            "Our goal was to design and build a water rocket that could travel the longest possible horizontal distance.",
        "What bottle did you use?":
            "We reused a 1.5-liter Mountain Dew soda bottle.",
        "What is the bottle's capacity?":
            "Our bottle has a capacity of 1.5 liters.",
        "How long is your rocket?":
            "Our final Golden Voyager is exactly 50 centimeters long.",
        "What materials did you use?":
            "We used a reused Mountain Dew soda bottle, cardboard from a reused plate for the fins, plastic document folder sheets for the nose cone, and duct tape.",
        "How far did your rocket travel?":
            "Our Golden Voyager traveled 41.8 meters during testing!",
        "At what angle was the rocket launched?":
            "Our rocket was launched at an angle of 45 degrees."
    },

    "2. Prototype 1": {
        "Tell me about Prototype 1": prototype1,
        "What was Prototype 1 like?":
            "Our first prototype used a 1.5-liter bottle and had a short, blunt, elliptical nose cone.",
        "Why did you choose a 1.5-liter bottle?":
            "We wanted a balance between having enough space for water and compressed air while keeping the rocket lightweight.",
        "What were the benefits of Prototype 1?":
            "It used a suitable bottle capacity and a short, blunt nose intended for subsonic flight.",
        "What were the problems with Prototype 1?":
            "The nose cone was rough and asymmetrical, and the fins were unevenly attached. Some fins fell off and had to be re-glued.",
        "Why did you change Prototype 1?":
            "We wanted to improve the rocket's aerodynamics, durability, and stability."
    },

    "3. Prototype 2": {
        "Tell me about Prototype 2": prototype2,
        "What improvements did you make in Prototype 2?":
            "We made the nose cone longer and smoother and used tape instead of glue to secure the fins.",
        "Why did you make the nose cone longer?":
            "The longer nose cone helped shift the rocket's center of mass forward, which can improve stability.",
        "Why did you use tape instead of glue?":
            "The fins on Prototype 1 came loose, so we used tape to make the attachments more secure.",
        "How much water did you use?":
            "We filled the 1.5-liter bottle with a little over one-third of its total volume.",
        "Was Prototype 2 successful?":
            "Yes! Prototype 2 traveled significantly farther than many other teams' rockets during testing.",
        "What was wrong with Prototype 2?":
            "Prototype 2 was 55 centimeters long, exceeding the maximum permitted length by 5 centimeters.",
        "Why was Prototype 2 more aerodynamic?":
            "Its smoother nose cone and sturdier construction improved the overall design compared with Prototype 1."
    },

    "4. Final Rocket Design": {
        "Tell me about the final model": final_model,
        "Why did you choose Prototype 2 for the final design?":
            "Prototype 2 performed well, so we kept most of its features while correcting the length and improving the fins.",
        "What changes did you make to the final rocket?":
            "We reduced the length to 50 centimeters, made the fins thinner, and measured their placement more carefully.",
        "What shape are the fins?":
            "Our fins have a tapered trapezoidal shape.",
        "Why did you choose trapezoidal fins?":
            "We chose tapered trapezoidal fins to help stabilize the rocket while keeping the design lightweight and relatively aerodynamic.",
        "Why are fins important?":
            "Fins help stabilize the rocket and reduce unwanted changes in direction during flight.",
        "Why did you use cardboard for the fins?":
            "Cardboard is lightweight, sturdy, and easy to shape. We also reused a cardboard plate to reduce waste.",
        "What material is the nose cone made of?":
            "Our nose cone is made from plastic document folder sheets.",
        "What shape is the final nose cone?":
            "Our final nose cone has a longer, smoother, generally conical shape based on Prototype 2.",
        "Why did you use plastic folder sheets?":
            "Plastic document folder sheets are lightweight, flexible, and easy to shape into a smooth nose cone.",
        "Why is symmetry important?":
            "Symmetry helps balance aerodynamic forces and reduces unwanted changes in direction.",
        "Why did you use duct tape?":
            "We used duct tape to secure the rocket's components, especially the fins.",
        "Why is a smooth nose cone important?":
            "A smooth nose cone helps air flow around the rocket and can reduce aerodynamic drag."
    },

    "5. Physics and Motion": {
        "How does a water rocket work?":
            "Compressed air pushes water out of the bottle. The expelled water creates an opposite reaction force that propels the rocket forward.",
        "What is thrust?":
            "Thrust is the force that propels the rocket forward when water is expelled backward.",
        "What is Newton's Third Law?":
            "Newton's Third Law states that every action has an equal and opposite reaction. As the rocket pushes water backward, the water pushes the rocket forward.",
        "How does pressure affect the rocket?":
            "Compressed air provides the pressure that pushes water out of the bottle and generates thrust.",
        "How does water volume affect performance?":
            "Water provides the mass expelled to generate thrust, but too much water leaves less space for compressed air.",
        "What is projectile motion?":
            "Projectile motion describes the rocket's curved path under the influence of gravity after propulsion ends.",
        "How does gravity affect the rocket?":
            "Gravity continuously pulls the rocket downward, affecting its height, flight time, and horizontal distance.",
        "Why does launch angle matter?":
            "The launch angle affects the rocket's height and horizontal distance. Different angles produce different flight paths.",
        "Why did you launch at 45 degrees?":
            "We used 45 degrees to balance horizontal and vertical motion. In ideal projectile motion without air resistance, this angle gives maximum range when launch and landing heights are equal.",
        "What affects the rocket's flight distance?":
            "Launch angle, thrust, water volume, mass, air resistance, and stability all affect the rocket's flight distance."
    },

    "6. Aerodynamics and Stability": {
        "Why is aerodynamics important?":
            "Aerodynamics affects how air flows around the rocket. Reducing drag can help the rocket maintain speed and travel farther.",
        "What is air resistance?":
            "Air resistance, also called drag, is a force that opposes the rocket's motion through the air.",
        "What makes a rocket stable?":
            "A stable rocket generally has properly aligned fins and a center of mass positioned ahead of its center of pressure.",
        "What is the center of mass?":
            "The center of mass is the point where the rocket's mass can be considered concentrated.",
        "What is the center of pressure?":
            "The center of pressure is the point where the combined aerodynamic forces can be considered to act.",
        "How does the center of mass affect stability?":
            "For a typical fin-stabilized rocket, having the center of mass ahead of the center of pressure helps maintain stable flight.",
        "What is subsonic speed?":
            "Subsonic speed means traveling slower than the speed of sound.",
        "Why is nose cone shape important?":
            "The nose cone affects how air flows around the rocket. A smooth design can reduce drag, while its mass and length can also affect stability."
    },

    "7. Testing and Results": {
        "Was the final rocket successful?":
            "Yes! Our final Golden Voyager traveled 41.8 meters during testing.",
        "What were your final results?":
            "Our final rocket traveled 41.8 meters, meeting the 50-centimeter length requirement.",
        "What was the biggest problem with the final rocket?":
            "The fins may not have been perfectly symmetrical due to a possible measurement error, which could have affected the flight.",
        "Why did the rocket change direction?":
            "One possible reason is uneven fin spacing, which may have caused unbalanced aerodynamic forces.",
        "How could you improve the rocket?":
            "We could improve the accuracy of fin placement and spacing to increase stability and potentially improve flight distance.",
        "What did you learn from testing?":
            "We learned that small design details, such as fin alignment, nose cone shape, and rocket length, can affect performance."
    },

    "8. Safety and Sustainability": {
        "What safety precautions are important?":
            "Rocket launches should be supervised and conducted in a clear, designated area away from spectators.",
        "How is your rocket sustainable?":
            "Our Golden Voyager is environmentally sustainable because we reused a soda bottle and a cardboard plate instead of using entirely new materials. This reduces waste and gives existing materials a second purpose. Our design is also easy to recreate because these materials are affordable and widely available.",
        "Why did you reuse a soda bottle?":
            "We reused a 1.5-liter Mountain Dew soda bottle because it provided a suitable capacity for our water rocket. Reusing the bottle also helped reduce plastic waste.",
        "Why did you reuse a cardboard plate?":
            "We reused a cardboard plate to make our rocket's fins. Cardboard is lightweight, easy to cut, and suitable for our design. Reusing it also helped reduce waste.",
        "Why is sustainability important?":
            "Sustainability is important because it encourages us to reduce waste, reuse resources, and consider the environmental impact of our designs.",
        "Is your rocket easy to recreate?":
            "Yes! Our Golden Voyager uses common materials such as a soda bottle, cardboard, plastic folder sheets, and duct tape. These materials are affordable and accessible, making the design achievable and easy to reproduce.",
        "How does your rocket demonstrate sustainable engineering?":
            "Our rocket demonstrates sustainable engineering by reusing a soda bottle and a cardboard plate, reducing waste, and using accessible materials. This makes the design more environmentally responsible and practical to recreate.",
        "What is reproducibility?":
            "Reproducibility means that a design can be recreated using the same methods and materials. Our rocket is relatively easy to reproduce because its materials are common and affordable.",
        "How is your rocket affordable?":
            "Our rocket uses inexpensive, widely available materials, including a reused soda bottle and cardboard plate. This makes it achievable without expensive equipment or specialized construction materials."
    }
}

# ==========================================
# 4. ALTERNATIVE QUESTION PHRASES
# ==========================================

aliases = {
    "Tell me about Prototype 1": [
        "tell me about prototype 1",
        "explain prototype 1",
        "describe prototype 1",
        "prototype 1 overview",
        "tell me about the first prototype",
        "explain the first prototype"
    ],
    "Tell me about Prototype 2": [
        "tell me about prototype 2",
        "explain prototype 2",
        "describe prototype 2",
        "prototype 2 overview",
        "tell me about the second prototype",
        "explain the second prototype"
    ],
    "Tell me about the final model": [
        "tell me about the final model",
        "explain the final model",
        "describe the final model",
        "final model overview",
        "tell me about the final rocket",
        "explain the final rocket"
    ],
    "What is your rocket's name?": [
        "rocket name", "name of the rocket",
        "name of your rocket", "rocket called"
    ],
    "What is your chatbot's name?": [
        "your name", "who are you",
        "chatbot name", "bot name"
    ],
    "What bottle did you use?": [
        "which bottle", "type of bottle",
        "mountain dew bottle"
    ],
    "What is the bottle's capacity?": [
        "bottle capacity", "how many liters",
        "capacity of the bottle", "bottle size"
    ],
    "How long is your rocket?": [
        "rocket length", "how long",
        "50 cm", "50 centimeters"
    ],
    "What materials did you use?": [
        "what materials", "materials used",
        "rocket made of"
    ],
    "How far did your rocket travel?": [
        "how far", "flight distance",
        "distance traveled", "41.8 meters",
        "how many meters"
    ],
    "At what angle was the rocket launched?": [
        "launch angle", "angle launched",
        "what angle", "which angle"
    ],
    "Why did you launch at 45 degrees?": [
        "why 45", "why 45 degrees",
        "reason for 45"
    ],
    "What were the problems with Prototype 1?": [
        "prototype 1 problems",
        "first prototype drawbacks",
        "problems with the first prototype"
    ],
    "What improvements did you make in Prototype 2?": [
        "prototype 2 improvements",
        "changes in prototype 2",
        "second prototype improvements"
    ],
    "What was wrong with Prototype 2?": [
        "prototype 2 drawbacks",
        "prototype 2 problem",
        "why was prototype 2 too long"
    ],
    "What changes did you make to the final rocket?": [
        "final design changes",
        "final model improvements",
        "changes to the final model"
    ],
    "What shape are the fins?": [
        "fin shape", "shape of the fins",
        "what shape are your fins"
    ],
    "Why did you choose trapezoidal fins?": [
        "why trapezoid", "why trapezoidal",
        "why that fin shape",
        "why did you choose the fin shape"
    ],
    "Why are fins important?": [
        "purpose of fins", "why fins",
        "what do fins do", "how do fins work"
    ],
    "Why did you use cardboard for the fins?": [
        "why cardboard", "fin material",
        "what are the fins made of"
    ],
    "What material is the nose cone made of?": [
        "nose cone material", "tip material",
        "what is the nose made of"
    ],
    "What shape is the final nose cone?": [
        "nose shape", "tip shape",
        "shape of the nose cone"
    ],
    "How much water did you use?": [
        "water amount", "amount of water",
        "how much water", "water quantity"
    ],
    "How does a water rocket work?": [
        "how does the rocket work",
        "how do water rockets work",
        "how does it launch"
    ],
    "What is Newton's Third Law?": [
        "newton third law", "newtons third law",
        "action and reaction"
    ],
    "What is thrust?": [
        "define thrust", "how does thrust work"
    ],
    "Why is aerodynamics important?": [
        "importance of aerodynamics",
        "why aerodynamics", "aerodynamic design"
    ],
    "What is air resistance?": [
        "what is drag", "air resistance",
        "define drag"
    ],
    "What is projectile motion?": [
        "explain projectile motion",
        "projectile motion"
    ],
    "What makes a rocket stable?": [
        "rocket stability", "how to keep it stable",
        "what makes it stable"
    ],
    "What is the center of mass?": [
        "center of mass", "centre of mass"
    ],
    "What is the center of pressure?": [
        "center of pressure", "centre of pressure"
    ],
    "What were your final results?": [
        "final results", "testing results",
        "results of the rocket"
    ],
    "Was the final rocket successful?": [
        "was it successful", "did it work",
        "rocket success"
    ],
    "Why did the rocket change direction?": [
        "why did it turn", "why did it veer",
        "change direction"
    ],
    "How could you improve the rocket?": [
        "future improvements", "improve the rocket",
        "what would you change"
    ],
    "How is your rocket sustainable?": [
        "how is it sustainable",
        "sustainability of the rocket",
        "recycled materials",
        "environmentally friendly"
    ],
    "Why did you reuse a soda bottle?": [
        "why reuse a bottle",
        "reused soda bottle",
        "why recycled bottle"
    ],
    "Why did you reuse a cardboard plate?": [
        "why reuse cardboard",
        "reused cardboard plate",
        "why cardboard plate"
    ],
    "Is your rocket easy to recreate?": [
        "easy to recreate",
        "can you recreate it",
        "is it achievable",
        "easy to reproduce"
    ],
    "How does your rocket demonstrate sustainable engineering?": [
        "sustainable engineering",
        "environmental benefits",
        "environmentally sustainable"
    ],
    "What is reproducibility?": [
        "define reproducibility",
        "what does reproducibility mean",
        "reproducibility"
    ],
    "How is your rocket affordable?": [
        "affordable materials",
        "why is it affordable",
        "low cost design"
    ],
    "What safety precautions are important?": [
        "safety", "precautions", "safe launch"
    ]
}

# ==========================================
# 5. RULE-BASED QUESTION MATCHING
# ==========================================

UNKNOWN_MESSAGE = (
    "Hmm, I'm not sure about that question yet! "
    "Try asking about our rocket's design, "
    "prototypes, physics, sustainability, "
    "or testing results. "
    "Explore the questions in the sidebar!"
)

def clean_text(text):
    text = text.lower().replace("'", "")
    text = re.sub(r"[^a-z0-9 ]", " ", text)
    return " ".join(text.split())


def find_answer(question):
    q = clean_text(question)

    if q in [
        "hi", "hello", "hey",
        "good morning", "good afternoon"
    ]:
        return (
            "Hello! Welcome aboard! "
            "What would you like to know "
            "about the Golden Voyager?"
        )

    if q in [
        "thanks", "thank you",
        "thank you so much"
    ]:
        return (
            "You're very welcome! "
            "Do you have any other questions?"
        )

    all_prototypes = [
        "all prototypes",
        "all three prototypes",
        "all 3 prototypes",
        "rocket development",
        "evolution of the rocket",
        "all the prototypes",
        "compare the prototypes",
        "explain all three prototypes"
    ]

    if any(phrase in q for phrase in all_prototypes):
        return (
            prototype1 + "\n\n" +
            prototype2 + "\n\n" +
            final_model
        )

    # Exact question matching
    for questions in categories.values():
        for original, answer in questions.items():
            if q == clean_text(original):
                return answer

    # Alternative phrase matching
    matches = []

    for original, phrases in aliases.items():
        for phrase in phrases:
            normalized = clean_text(phrase)

            if normalized in q:
                matches.append(
                    (len(normalized), original)
                )

    if matches:
        matches.sort(reverse=True)
        selected = matches[0][1]

        for questions in categories.values():
            if selected in questions:
                return questions[selected]

    return UNKNOWN_MESSAGE


# ==========================================
# 6. AI KNOWLEDGE BASE
# ==========================================

PROJECT_KNOWLEDGE = f"""
You are Golden Companion, a friendly AI
assistant for the Golden Voyager water rocket.

Your purpose is to explain our engineering
project to students and visitors.

ROCKET INFORMATION:
Name: {rocket_info['name']}
Bottle: {rocket_info['bottle']}
Final length: {rocket_info['length']}
Flight distance: {rocket_info['distance']}
Launch angle: {rocket_info['angle']}
Fin shape: {rocket_info['fin_shape']}
Fin material: {rocket_info['fin_material']}
Nose cone material: {rocket_info['nose_material']}
Attachment: {rocket_info['attachment']}

COMPLETE PROJECT DEVELOPMENT:

{prototype1}

{prototype2}

{final_model}

PROGRAMMED QUESTIONS AND ANSWERS:
"""

for category, questions in categories.items():
    PROJECT_KNOWLEDGE += f"\n{category}\n"

    for question, answer in questions.items():
        PROJECT_KNOWLEDGE += (
            f"Question: {question}\n"
            f"Answer: {answer}\n\n"
        )

PROJECT_KNOWLEDGE += """
IMPORTANT INSTRUCTIONS:

1. You are Golden Companion, not a general
   purpose assistant.

2. Focus on the Golden Voyager water rocket,
   engineering, aerodynamics, physics,
   sustainability, and project results.

3. Answer naturally and clearly.

4. Use simple explanations suitable for
   students and project visitors.

5. Do not invent project measurements,
   experimental results, or materials.

6. If a specific project detail is unknown,
   say that the information was not provided.

7. Explain general engineering principles
   when they help answer a question.

8. Keep most responses between two and
   five sentences unless the visitor asks
   for a detailed explanation.

9. For unrelated questions, politely explain
   that your main purpose is to discuss
   the Golden Voyager project.

10. Be friendly, professional, and helpful.

11. Do not confuse the 1.5-liter bottle
    capacity with the 50-centimeter
    physical rocket length.

12. The rocket traveled 41.8 meters.
    Do not invent additional test results.

13. The final rocket was launched at
    45 degrees.

14. The final rocket reused a soda bottle
    and a cardboard plate to reduce waste.

15. The final rocket's fins may have been
    slightly asymmetrical, which could
    explain its deviation in flight.

16. Do not claim that an explanation is
    a confirmed experimental finding
    unless the project information says so.
"""


# ==========================================
# 7. HYBRID AI RESPONSE SYSTEM
# ==========================================

def hybrid_answer(question):
    # Answer known project questions without making a paid API request.
    original_answer = find_answer(question)
    if original_answer != UNKNOWN_MESSAGE:
        return original_answer, "Programmed answer"

    # Use OpenAI only when no programmed answer matches.
    try:
        api_key = st.secrets.get("OPENAI_API_KEY", "")
        if not api_key:
            return (
                "OpenAI is not connected yet. Add OPENAI_API_KEY to your "
                "Streamlit app secrets. The programmed rocket questions still work!",
                "AI unavailable",
            )

        client = OpenAI(api_key=api_key, timeout=25.0, max_retries=1)
        response = client.responses.create(
            model="gpt-4.1-mini",
            instructions=PROJECT_KNOWLEDGE,
            input=question,
            max_output_tokens=800,
        )
        answer = (response.output_text or "").strip()
        if answer:
            return answer, "AI-generated answer"
        return "OpenAI did not return an answer. Please try again.", "AI unavailable"

    except Exception as exc:
        # Keep private credentials and API error details out of the public page.
        print("OpenAI request failed:", type(exc).__name__)
        return (
            "OpenAI is temporarily unavailable. Please check your API key, "
            "credit balance, and model access. The programmed rocket "
            "questions still work!",
            "AI unavailable",
        )


# ==========================================
# 8. SPACE THEME AND GOLDEN PLANET
# ==========================================

st.markdown("""
<style>

/* SPACE BACKGROUND */

.stApp {
    background:
        radial-gradient(
            circle at 75% 22%,
            rgba(191, 128, 49, 0.10),
            transparent 30%
        ),
        radial-gradient(
            circle at 18% 70%,
            rgba(38, 71, 123, 0.24),
            transparent 40%
        ),
        #080f20;

    color: #f7f2e8;
}

/* TWINKLING STAR FIELD - multiple layers with different star sizes */
.stApp {
    isolation: isolate;
}
.stApp > .main::before,
[data-testid="stAppViewContainer"]::before {
    content: "";
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 0;
    background-image:
        radial-gradient(1.5px 1.5px at 6% 12%, #ffffff 98%, transparent),
        radial-gradient(2px 2px at 17% 27%, #ffebba 98%, transparent),
        radial-gradient(1px 1px at 28% 8%, #ffffff 98%, transparent),
        radial-gradient(1.5px 1.5px at 39% 41%, #ffffff 98%, transparent),
        radial-gradient(1px 1px at 52% 19%, #fff2cf 98%, transparent),
        radial-gradient(2px 2px at 66% 35%, #ffffff 98%, transparent),
        radial-gradient(1px 1px at 79% 9%, #ffffff 98%, transparent),
        radial-gradient(1.5px 1.5px at 92% 32%, #ffdf9c 98%, transparent),
        radial-gradient(1px 1px at 11% 62%, #ffffff 98%, transparent),
        radial-gradient(2px 2px at 23% 80%, #ffffff 98%, transparent),
        radial-gradient(1px 1px at 34% 69%, #ffffff 98%, transparent),
        radial-gradient(1.5px 1.5px at 46% 89%, #ffebba 98%, transparent),
        radial-gradient(1px 1px at 59% 58%, #ffffff 98%, transparent),
        radial-gradient(2px 2px at 71% 78%, #ffffff 98%, transparent),
        radial-gradient(1px 1px at 84% 65%, #ffffff 98%, transparent),
        radial-gradient(1.5px 1.5px at 96% 91%, #ffffff 98%, transparent);
    background-size: 420px 370px;
    opacity: .8;
    animation: twinkleStars 5s ease-in-out infinite alternate;
}
@keyframes twinkleStars {
    from { opacity: .30; }
    to { opacity: .95; }
}
@media (prefers-reduced-motion: reduce) {
    [data-testid="stAppViewContainer"]::before { animation: none; }
}

/* GOLDEN SATURN PLANET */

.stApp::before {
    content: "";
    position: fixed;
    top: 17%;
    right: 7%;
    width: 205px;
    height: 205px;
    border-radius: 50%;

    background:
        radial-gradient(
            circle at 30% 28%,
            #ffe6ad 0%,
            #e8b777 25%,
            #bb7747 55%,
            #493149 85%,
            #17172d 100%
        );

    box-shadow:
        0 0 55px rgba(233, 170, 81, 0.15),
        inset -20px -16px 35px
        rgba(11, 14, 35, 0.50);

    pointer-events: none;
    z-index: 0;
    opacity: 0.90;
}

/* SATURN RING */

.stApp::after {
    content: "";
    position: fixed;
    top: calc(17% + 72px);
    right: calc(7% - 46px);
    width: 295px;
    height: 60px;

    border: 9px solid rgba(
        245, 194, 117, 0.85
    );

    border-radius: 50%;
    transform: rotate(-24deg);

    box-shadow:
        0 0 15px rgba(250, 193, 103, 0.28);

    pointer-events: none;
    z-index: 0;
}

/* KEEP CONTENT ABOVE BACKGROUND */

.block-container {
    position: relative;
    z-index: 1;
    padding-top: 3rem;
}

/* GOLD TITLES */

h1, h2, h3 {
    color: #f5c451 !important;
}

h1 {
    font-weight: 800 !important;
    text-shadow:
        0 0 22px rgba(255, 193, 80, 0.22);
}

/* GENERAL TEXT */

p, label {
    color: #f3e9d5;
}

/* SIDEBAR */

[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #111e36,
            #0a1225
        );
    border-right:
        1px solid rgba(245, 196, 81, 0.3);
}

/* SIDEBAR EXPANDERS */

[data-testid="stExpander"] {
    border:
        1px solid rgba(231, 178, 82, 0.55);
    border-radius: 12px;
    background: rgba(18, 34, 60, 0.65);
}

/* CHAT MESSAGES */

[data-testid="stChatMessage"] {
    background:
        rgba(19, 31, 55, 0.88);

    border:
        1px solid rgba(221, 164, 64, 0.55);

    border-radius: 15px;
    margin-bottom: 12px;

    box-shadow:
        0 0 18px rgba(217, 168, 58, 0.08);
}

/* BUTTONS */

.stButton > button {
    background:
        linear-gradient(
            135deg,
            #3b2d19,
            #1d233b
        );

    color: #ffe5a8;
    border: 1px solid #c59645;
    border-radius: 11px;

    width: 100%;
    height: auto;
    white-space: normal;
    text-align: left;

    padding: 10px;
}

.stButton > button:hover {
    border-color: #ffdc85;
    color: #fff5d5;
    background: #4b351c;
}

/* CHAT INPUT */

[data-testid="stChatInput"] {
    border:
        1px solid #c59645;
    border-radius: 13px;
}

/* PROJECT METRICS */

.metricbar {
    background:
        linear-gradient(
            90deg,
            rgba(31, 42, 67, 0.95),
            rgba(70, 48, 26, 0.80)
        );

    padding: 15px;
    border-radius: 13px;

    border: 1px solid #c59645;
    margin-bottom: 22px;

    color: #ffe6b4;
}

/* AI LABEL */

.ai-label {
    color: #d8b66c;
    font-size: 12px;
    margin-top: 4px;
}

/* DIVIDERS */

hr {
    border-color: #8c6b30;
}

/* MOBILE DISPLAY */

@media (max-width: 700px) {
    .stApp::before {
        width: 120px;
        height: 120px;
        right: 4%;
        top: 13%;
        opacity: 0.45;
    }

    .stApp::after {
        width: 170px;
        height: 38px;
        right: 0%;
        top: calc(13% + 42px);
        border-width: 5px;
        opacity: 0.45;
    }
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# 9. MAIN HEADER
# ==========================================

st.title("🚀 Golden Companion")

st.caption(
    "Your guide to the Golden Voyager "
    "• Water Rocket Challenge 2026"
)

st.markdown(
    """
    <div class="metricbar">
        🏁 <b>41.8 m</b> flight distance
        &nbsp; • &nbsp;
        📏 <b>50 cm</b> final length
        &nbsp; • &nbsp;
        ♻️ Reused materials
    </div>
    """,
    unsafe_allow_html=True
)


# ==========================================
# 10. CHAT HISTORY
# ==========================================

welcome_message = (
    "Hi there! Welcome aboard! "
    "I'm Golden Companion, your friendly "
    "hybrid AI rocket assistant. "
    "Ask me about our prototypes, "
    "final design, physics, results, "
    "or sustainability!"
)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": welcome_message,
            "source": "Welcome"
        }
    ]

if "pending_question" not in st.session_state:
    st.session_state.pending_question = None


# ==========================================
# 11. SIDEBAR QUESTION MENU
# ==========================================

with st.sidebar:

    st.header("🌌 Explore Our Rocket")

    st.write(
        "Choose a category, then click "
        "any question to ask it."
    )

    st.caption(
        f"{sum(len(q) for q in categories.values())} programmed questions + OpenAI AI"
    )

    for category, questions in categories.items():

        with st.expander(category):

            for idx, question in enumerate(questions):

                if st.button(
                    question,
                    key=f"{category}-{idx}"
                ):
                    st.session_state.pending_question = (
                        question
                    )

    st.divider()

    if st.button("🚀 Explain all three prototypes"):
        st.session_state.pending_question = (
            "Explain all three prototypes"
        )

    if st.button("🧹 Clear conversation"):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": welcome_message,
                "source": "Welcome"
            }
        ]

        st.session_state.pending_question = None
        st.rerun()

    st.divider()

    st.caption(
        "Golden Companion uses programmed "
        "answers first and AI for unfamiliar "
        "questions when available."
    )


# ==========================================
# 12. DISPLAY CHAT MESSAGES
# ==========================================

for msg in st.session_state.messages:

    avatar = (
        "🚀"
        if msg["role"] == "assistant"
        else "👤"
    )

    with st.chat_message(
        msg["role"],
        avatar=avatar
    ):

        st.markdown(msg["content"])

        source = msg.get("source", "")

        if source == "AI-generated answer":
            st.caption("✨ AI-generated response")

        elif source == "Programmed answer":
            st.caption("📚 Project knowledge base")


# ==========================================
# 13. CHAT INPUT
# ==========================================

typed_question = st.chat_input(
    "Ask Golden Companion a question..."
)

question = (
    st.session_state.pending_question
    or typed_question
)

if question:

    st.session_state.pending_question = None

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.spinner(
        "Golden Companion is thinking..."
    ):
        answer, source = hybrid_answer(question)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
            "source": source
        }
    )

    st.rerun()