from flask import Flask, jsonify
import BAL.statsdata


def stats_data_service():

    app = Flask(__name__)
    # app.config["DEBUG"] = True

    @app.route('/v1/stats/data/full', methods=['GET'])
    def get_stats_data():
        return jsonify(BAL.statsdata.get_all_stats_data())

    @app.route('/v1/stats/data/students', methods=['GET'])
    def get_students():
        return jsonify(BAL.statsdata.get_student())

    @app.route('/v1/stats/data/province/<p>', methods=['GET'])
    def get_provinces(p):
        return jsonify(BAL.statsdata.get_province(p))

    @app.route('/v1/stats/data/lfs/<num>', methods=['GET'])
    def get_status(num):
        return jsonify(BAL.statsdata.get_lfstatus(num))

    @app.route('/', methods=['GET'])
    def home():
        return """<h1>Sales Statistics</h1><p>This site is a prototype API for reporting sales
         statistics for use with Python and Pandas clients.</p>"""

    app.run(host='0.0.0.0')