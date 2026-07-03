from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    routine = None
    skin_type = None
    concern = None
    budget = None
    products = []
    explanation = None

    if request.method == "POST":

        skin_type = request.form["skin_type"]
        concern = request.form["concern"]
        budget = request.form["budget"]

        

        if concern == "Acne":

            if skin_type == "Oily":
                routine = """Cleanser
Niacinamide
Oil-Free Moisturizer
SPF

🌙
Cleanser
Salicylic Acid
Gel Moisturizer"""

                explanation = "Oily acne-prone skin benefits from oil control and pore clearing. Niacinamide regulates sebum while salicylic acid clears pores deeply without stripping."

            elif skin_type == "Dry":
                routine = """Hydrating Cleanser
Niacinamide
Cream Moisturizer
SPF

🌙
Hydrating Cleanser
Azelaic Acid
Rich Moisturizer"""

                explanation = "Dry acne-prone skin needs hydration + gentle acne treatment. Azelaic acid reduces acne and inflammation without damaging the skin barrier."

            elif skin_type == "Combination":
                routine = """Gentle Cleanser
Niacinamide
Light Moisturizer
SPF

🌙
Cleanser
Salicylic Acid
Moisturizer"""

                explanation = "Combination skin needs balance — oil control in T-zone while maintaining hydration elsewhere."

            else:
                routine = """Gentle Cleanser
Niacinamide
Moisturizer
SPF

🌙
Cleanser
Salicylic Acid
Moisturizer"""

                explanation = "Balanced acne routine focusing on gentle cleansing, barrier support, and mild exfoliation."

        elif concern == "Dark spots":

            if skin_type == "Dry":
                routine = """Hydrating Cleanser
Vitamin C
Moisturizer
SPF

🌙
Cleanser
Niacinamide
Hydrating Serum
Rich Moisturizer"""
            else:
                routine = """Cleanser
Vitamin C
Moisturizer
SPF

🌙
Cleanser
Niacinamide
Treatment Serum
Moisturizer"""

            explanation = "Vitamin C brightens pigmentation in the morning while niacinamide supports overnight repair and evens skin tone."

        elif concern == "Dryness":

            if skin_type == "Oily":
                routine = """Gentle Cleanser
Hyaluronic Acid
Gel Moisturizer
SPF

🌙
Cleanser
Hydrating Serum
Light Moisturizer"""
            else:
                routine = """Hydrating Cleanser
Hyaluronic Acid
Rich Moisturizer
SPF

🌙
Cleanser
Hydrating Serum
Rich Moisturizer"""

            explanation = "Hydration-focused routine that rebuilds moisture and strengthens the skin barrier."

        else:

            routine = """Gentle Cleanser
Niacinamide
Moisturizer
SPF

🌙
Cleanser
Repair Serum
Moisturizer"""

            explanation = "Barrier-support routine designed for overall skin health and long-term balance."

        

        if budget == "Under $15":

            if concern == "Acne":
                products = [
                    "CeraVe Foaming Cleanser",
                    "The Ordinary Niacinamide 10%",
                    "Differin Gel",
                    "Neutrogena SPF 30"
                ]

            elif concern == "Dark spots":
                products = [
                    "Good Molecules Vitamin C Serum",
                    "The Ordinary Niacinamide 10%",
                    "CeraVe Moisturizing Cream",
                    "Neutrogena SPF 30"
                ]

            elif concern == "Dryness":
                products = [
                    "CeraVe Hydrating Cleanser",
                    "The Ordinary Hyaluronic Acid",
                    "CeraVe Moisturizing Cream",
                    "Neutrogena SPF 30"
                ]

            else:
                products = [
                    "Cetaphil Gentle Cleanser",
                    "The Ordinary Niacinamide 10%",
                    "Simple Moisturizer",
                    "Neutrogena SPF 30"
                ]

        elif budget == "$15 - $30":

            if concern == "Acne":
                products = [
                    "Paula's Choice 2% BHA",
                    "CeraVe PM Lotion",
                    "La Roche-Posay Cleanser",
                    "Beauty of Joseon SPF"
                ]

            elif concern == "Dark spots":
                products = [
                    "Paula's Choice Vitamin C",
                    "CeraVe PM Lotion",
                    "The Ordinary Alpha Arbutin",
                    "La Roche-Posay SPF"
                ]

            elif concern == "Dryness":
                products = [
                    "La Roche-Posay Hydrating Cleanser",
                    "Hyaluronic Acid Serum",
                    "CeraVe Moisturizing Cream",
                    "Beauty of Joseon SPF"
                ]

            else:
                products = [
                    "CeraVe Cleanser",
                    "Niacinamide Serum",
                    "Neutrogena Hydro Boost",
                    "La Roche-Posay SPF"
                ]

        else:  # $30+

            if concern == "Acne":
                products = [
                    "SkinCeuticals Blemish + Age Defense",
                    "EltaMD UV Clear SPF 46",
                    "La Roche-Posay Effaclar Cleanser",
                    "Paula's Choice BHA 2%"
                ]

            elif concern == "Dark spots":
                products = [
                    "SkinCeuticals Discoloration Defense",
                    "Obagi Vitamin C Serum",
                    "EltaMD UV Clear SPF 46",
                    "Drunk Elephant Moisturizer"
                ]

            elif concern == "Dryness":
                products = [
                    "Drunk Elephant Lala Retro Cream",
                    "SkinCeuticals Hydrating B5",
                    "La Roche-Posay Gentle Cleanser",
                    "EltaMD UV Clear SPF 46"
                ]

            else:
                products = [
                    "Tatcha Water Cream",
                    "SkinCeuticals Serum",
                    "EltaMD SPF",
                    "Drunk Elephant Cleanser"
                ]

    return render_template(
        "index.html",
        routine=routine,
        skin_type=skin_type,
        concern=concern,
        budget=budget,
        products=products,
        explanation=explanation
    )


if __name__ == "__main__":
    app.run(debug=True)