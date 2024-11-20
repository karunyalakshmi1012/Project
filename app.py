from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enables Cross-Origin Resource Sharing for local testing

# Sample recommendations data
recommendations_data = {
    "Chennai": {
        "Friends": {
            "Morning": ["Marina Beach", "Elliot's Beach", "Guindy National Park"],
            "Afternoon": ["Express Avenue Mall", "VGP Universal Kingdom", "Phoenix Mall"],
            "Evening": ["Besant Nagar", "MGM Beach Resort", "ECR Restaurants"],
            "Night": ["Pondy Bazaar", "Night Drive on ECR", "Alcove", "Skywalk Mall"]
        },
        "Family": {
            "Morning": ["Dakshinachitra", "Birla Planetarium", "Arignar Anna Zoological Park"],
            "Afternoon": ["VGP Universal Kingdom", "Sri Parthasarathy Temple", "Government Museum"],
            "Evening": ["ECR Restaurants", "Elliot's Beach", "Lighthouse Visit"],
            "Night": ["Drive-in cinema", "Night Markets", "Pondy Bazaar"]
        },
        "Partner": {
            "Morning": ["Muttukadu Boat House", "Guindy National Park", "Kapaleeshwarar Temple"],
            "Afternoon": ["Phoenix Mall", "Theosophical Society", "San Thome Cathedral"],
            "Evening": ["ECR Restaurants", "Lighthouse Visit", "Marina Beach"],
            "Night": ["Night Drive", "Pondy Bazaar", "Skywalk Mall"]
        },
        "Alone": {
            "Morning": ["Kapaleeshwarar Temple", "Guindy National Park", "Birla Planetarium"],
            "Afternoon": ["Government Museum", "Phoenix Mall", "Elliot's Beach"],
            "Evening": ["Lighthouse Visit", "ECR Restaurants", "Express Avenue Mall"],
            "Night": ["Pondy Bazaar", "Night Drive", "Alcove"]
        }
    },
    "Coimbatore": {
        "Friends": {
            "Morning": ["VOC Park", "Perur Pateeswarar Temple", "Isha Yoga Center"],
            "Afternoon": ["Brookefields Mall", "Bennet's Hotel", "Marudamalai Temple"],
            "Evening": ["Tidel Park", "Kovai Kutralam Waterfall", "Aliyar Dam"],
            "Night": ["Brookefields Mall", "Kovai Kutralam Waterfall", "Fun Republic Mall"]
        },
        "Family": {
            "Morning": ["Isha Yoga Center", "Perur Pateeswarar Temple", "Marudamalai Temple"],
            "Afternoon": ["Brookefields Mall", "Bennet's Hotel", "Aliyar Dam"],
            "Evening": ["Kovai Kutralam Waterfall", "Tidel Park", "VOC Park"],
            "Night": ["Fun Republic Mall", "Tidel Park", "Brookefields Mall"]
        },
        "Partner": {
            "Morning": ["Isha Yoga Center", "Perur Pateeswarar Temple", "Kovai Kutralam Waterfall"],
            "Afternoon": ["Bennet's Hotel", "Aliyar Dam", "Brookefields Mall"],
            "Evening": ["Tidel Park", "Kovai Kutralam Waterfall", "Fun Republic Mall"],
            "Night": ["Night drive", "Fun Republic Mall", "Kovai Kutralam Waterfall"]
        },
        "Alone": {
            "Morning": ["Perur Pateeswarar Temple", "VOC Park", "Isha Yoga Center"],
            "Afternoon": ["Brookefields Mall", "Marudamalai Temple", "Aliyar Dam"],
            "Evening": ["Kovai Kutralam Waterfall", "Tidel Park", "Bennet's Hotel"],
            "Night": ["Night drive", "Fun Republic Mall", "Tidel Park"]
        }
    },
    "Vellore": {
        "Friends": {
            "Morning": ["Vellore Fort", "Sripuram Golden Temple", "Amirthi Zoo"],
            "Afternoon": ["Bazaars", "VIT University Campus", "Chellapalli Lake"],
            "Evening": ["Kallapalli Lake", "Vellore Fort", "Golden Temple"],
            "Night": ["Night Walk around Vellore Fort", "Cafe Outlets", "Local Markets"]
        },
        "Family": {
            "Morning": ["Sripuram Golden Temple", "Vellore Fort", "Chellapalli Lake"],
            "Afternoon": ["VIT University", "Bazaars", "Amirthi Zoo"],
            "Evening": ["Kallapalli Lake", "Golden Temple", "Vellore Fort"],
            "Night": ["Night Markets", "Cafe Outlets", "Local Restaurants"]
        },
        "Partner": {
            "Morning": ["Golden Temple", "Vellore Fort", "Amirthi Zoo"],
            "Afternoon": ["VIT University", "Bazaars", "Chellapalli Lake"],
            "Evening": ["Kallapalli Lake", "Golden Temple", "Vellore Fort"],
            "Night": ["Cafe Outlets", "Night Walk around Vellore Fort", "Local Markets"]
        },
        "Alone": {
            "Morning": ["Vellore Fort", "Golden Temple", "Amirthi Zoo"],
            "Afternoon": ["Chellapalli Lake", "VIT University", "Bazaars"],
            "Evening": ["Kallapalli Lake", "Vellore Fort", "Golden Temple"],
            "Night": ["Night Markets", "Cafe Outlets", "Local Markets"]
        }
    },
    "Bangalore": {
        "Friends": {
            "Morning": ["Cubbon Park", "Bannerghatta National Park", "Nandi Hills"],
            "Afternoon": ["Bangalore Palace", "Vidhana Soudha", "Lalbagh Botanical Garden"],
            "Evening": ["MG Road", "Brigade Road", "UB City"],
            "Night": ["Indiranagar", "Koramangala", "Church Street"]
        },
        "Family": {
            "Morning": ["Bannerghatta National Park", "Cubbon Park", "Nandi Hills"],
            "Afternoon": ["Bangalore Palace", "Vidhana Soudha", "Lalbagh Botanical Garden"],
            "Evening": ["MG Road", "UB City", "Brigade Road"],
            "Night": ["Koramangala", "Church Street", "Indiranagar"]
        },
        "Partner": {
            "Morning": ["Cubbon Park", "Bannerghatta National Park", "Nandi Hills"],
            "Afternoon": ["Bangalore Palace", "Lalbagh Botanical Garden", "Vidhana Soudha"],
            "Evening": ["UB City", "MG Road", "Brigade Road"],
            "Night": ["Koramangala", "Church Street", "Indiranagar"]
        },
        "Alone": {
            "Morning": ["Nandi Hills", "Cubbon Park", "Bannerghatta National Park"],
            "Afternoon": ["Bangalore Palace", "Lalbagh Botanical Garden", "Vidhana Soudha"],
            "Evening": ["MG Road", "Brigade Road", "UB City"],
            "Night": ["Indiranagar", "Koramangala", "Church Street"]
        }
    },
    "Kerala": {
        "Friends": {
            "Morning": ["Alleppey Backwaters", "Munnar Tea Gardens", "Athirappilly Waterfalls"],
            "Afternoon": ["Kochi Fort", "Kumarakom", "Vypin Island"],
            "Evening": ["Kovalam Beach", "Alappuzha Beach", "Varkala Beach"],
            "Night": ["Kochi", "Trivandrum", "Varkala"]
        },
        "Family": {
            "Morning": ["Alleppey Backwaters", "Munnar Tea Gardens", "Athirappilly Waterfalls"],
            "Afternoon": ["Kochi Fort", "Kumarakom", "Vypin Island"],
            "Evening": ["Kovalam Beach", "Alappuzha Beach", "Varkala Beach"],
            "Night": ["Trivandrum", "Varkala", "Kochi"]
        },
        "Partner": {
            "Morning": ["Munnar Tea Gardens", "Alleppey Backwaters", "Athirappilly Waterfalls"],
            "Afternoon": ["Vypin Island", "Kumarakom", "Kochi Fort"],
            "Evening": ["Kovalam Beach", "Alappuzha Beach", "Varkala Beach"],
            "Night": ["Kochi", "Varkala", "Trivandrum"]
        },
        "Alone": {
            "Morning": ["Munnar Tea Gardens", "Alleppey Backwaters", "Athirappilly Waterfalls"],
            "Afternoon": ["Vypin Island", "Kumarakom", "Kochi Fort"],
            "Evening": ["Alappuzha Beach", "Varkala Beach", "Kovalam Beach"],
            "Night": ["Trivandrum", "Kochi", "Varkala"]
        }
    },
"Mumbai": {
        "Friends": {
            "Morning": ["Marine Drive", "Gateway of India", "Elephanta Caves"],
            "Afternoon": ["Colaba Causeway", "Bandra Bandstand", "Chor Bazaar"],
            "Evening": ["Juhu Beach", "Bandra-Worli Sea Link", "Carter Road"],
            "Night": ["Colaba", "Marine Drive", "Bandra"]
        },
        "Family": {
            "Morning": ["Gateway of India", "Elephanta Caves", "Marine Drive"],
            "Afternoon": ["Colaba Causeway", "Juhu Beach", "Chor Bazaar"],
            "Evening": ["Bandra-Worli Sea Link", "Carter Road", "Juhu Beach"],
            "Night": ["Marine Drive", "Bandra", "Colaba"]
        },
        "Partner": {
            "Morning": ["Gateway of India", "Marine Drive", "Elephanta Caves"],
            "Afternoon": ["Colaba Causeway", "Chor Bazaar", "Bandra Bandstand"],
            "Evening": ["Juhu Beach", "Bandra-Worli Sea Link", "Carter Road"],
            "Night": ["Marine Drive", "Bandra", "Colaba"]
        },
        "Alone": {
            "Morning": ["Marine Drive", "Gateway of India", "Elephanta Caves"],
            "Afternoon": ["Bandra Bandstand", "Chor Bazaar", "Colaba Causeway"],
            "Evening": ["Carter Road", "Bandra-Worli Sea Link", "Juhu Beach"],
            "Night": ["Marine Drive", "Bandra", "Colaba"]
        }
    }
}




# Endpoint to get recommendations
@app.route('/recommend', methods=['GET'])
def recommend():
    city = request.args.get('city')
    with_whom = request.args.get('with_whom')
    time = request.args.get('time')

    if not (city and with_whom and time):
        return jsonify({"error": "Missing parameters"}), 400

    try:
        recommendation = recommendations_data[city][with_whom][time]
        return jsonify({"recommendation": recommendation})
    except KeyError:
        return jsonify({"error": "No recommendations found for the given parameters"}), 404


if __name__ == '__main__':
    app.run(debug=True)