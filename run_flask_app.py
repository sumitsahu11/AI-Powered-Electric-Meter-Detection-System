import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from app.app import create_app

if __name__ == '__main__':
    app = create_app()
    
    print("\n" + "="*60)
    print("🚀 Flask App is running!")
    print("📍 Open your browser: http://localhost:5000")
    print("🛑 To stop: Press CTRL + C")
    print("="*60 + "\n")
    
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=False,
        use_reloader=False
    )
