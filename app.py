from flask import Flask, request, render_template
import pandas as pd
import joblib


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    
    if request.method == "POST":
        
        clf = joblib.load("clf.pkl")
        
        gender = request.form.get("gender")
        age = int(request.form.get("age"))
        form = request.form.get("form")
        education = int(request.form.get("education"))
        group_of_disability = int(request.form.get("group_of_disability"))
        disease_duration = float(request.form.get("disease_duration"))
        connection_with_stress = int(request.form.get("connection_with_stress"))
        HPT_9_right = float(request.form.get("9_HPT_right"))
        HPT_9_left = float(request.form.get("9_HPT_left"))
        foot_25_test = float(request.form.get("25_foot_test"))
        EDSS = float(request.form.get("EDSS"))
        plasmapheresis = int(request.form.get("plasmapheresis"))
        DMT = int(request.form.get("DMT"))
        MOCA_score = int(request.form.get("MOCA_score"))
        SDMT_percent = float(request.form.get("SDMT_percent"))
        schulte_efficiency = int(request.form.get("schulte_efficiency"))
        schulte_adaptability = float(request.form.get("schulte_adaptability"))
        schulte_psychic_resist = float(request.form.get("schulte_psychic_resist"))
        SF36_psychic = float(request.form.get("SF-36_psychic"))
        SF36_physical = float(request.form.get("SF-36_physical"))

        
        X = pd.DataFrame([[gender, age, form, education, group_of_disability, disease_duration, connection_with_stress,
        HPT_9_right, HPT_9_left, foot_25_test, EDSS, plasmapheresis, DMT, 
        MOCA_score, SDMT_percent, schulte_efficiency, schulte_adaptability, 
        schulte_psychic_resist, SF36_psychic, SF36_physical]], columns = ["gender", "age", "form", "education", 
        "group_of_disability", "disease_duration", "connection_with_stress",
        "9_HPT_right", "9_HPT_left", "25_foot_test", "EDSS", "plasmapheresis", "DMT", 
        "MOCA_score", "SDMT_percent", "schulte_efficiency", "schulte_adaptability", 
        "schulte_psychic_resist", "SF-36_psychic", "SF-36_physical"])
        
        prediction = clf.predict(X)[0]
        if prediction == 0:
            text = "Риск депрессивных расстройств низкий"
        else:
            text = "Риск депрессивных расстройств высокий"
        
    else:
        text = ""
        
    return render_template("index.html", output=text)

if __name__ == '__main__':
    app.run(debug = True)
