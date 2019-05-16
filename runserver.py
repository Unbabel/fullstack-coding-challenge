"""
This script runs the UnbabelChallenge application using a development server.
"""

from import os
from UnbabelChallenge import app

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
