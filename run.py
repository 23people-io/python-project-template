import os

import uvicorn

if __name__ == "__main__":
    port_str = os.getenv("PORT")
    port = int(port_str) if port_str is not None else 8000
    uvicorn.run("main:app", host="127.0.0.1", port=port, reload=True)
