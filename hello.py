from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Global list to store usernames
usernames = []

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/who")
def who():
    # return "<p>Hello, World!</p>"
    # Display all usernames stored in the global list
    return jsonify({"usernames": usernames})


@app.route("/userdata", methods=['POST'])
def userdata():
    try:
        # Check the content type of the request
        if request.content_type == 'application/json':
            # Handle JSON data
            data = request.json
        elif request.content_type == 'application/x-www-form-urlencoded':
            # Handle form-encoded data
            data = request.form.to_dict()
        else:
            # Unsupported Media Type
            return jsonify({"error": "Unsupported Media Type. Expected application/json or application/x-www-form-urlencoded."}), 415
        
        # Displaying the entire request data
        print("Received request data:", data)
        
        # Extract specific fields, e.g., userName and password
        userName = data.get('userName')
        password = data.get('password')
        print(f"Received userName: {userName}, password: {password}")
        
        # Add the userName to the global list if it's not None
        if userName:
            usernames.append(userName)
        

        # Return the extracted data in the response
        # return jsonify({"userName": userName, "password": password}), 200
        return jsonify({"userName": userName, "password": "xxxxx"}), 200



    except Exception as e:
        print("Error:", e)
        # Returning a 404 status code in case of an error
        return jsonify({"error": "An error occurred while processing the request."}), 404

if __name__ == '__main__':
      app.run(debug=True)