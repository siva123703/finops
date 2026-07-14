import os
from pathlib import Path

import functions_framework
from flask import Flask, jsonify, render_template, request

from src.orchestrator.orchestrator import FinOpsOrchestrator

app = Flask(__name__, template_folder=str(Path(__file__).resolve().parent.parent / "templates"))


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    orchestrator = FinOpsOrchestrator()
    payload = request.get_json(silent=True) or {}
    user_message = payload.get("message") or payload.get("prompt") or ""

    if user_message:
        result = orchestrator.run(user_message=user_message)
    else:
        result = orchestrator.run()

    return jsonify(result)


@functions_framework.http
def finops_agent(request):
    """
    Cloud Function entry point for the FinOps chatbot agent.
    """

    orchestrator = FinOpsOrchestrator()

    try:
        if request is None:
            result = orchestrator.run()
            return result

        if not hasattr(request, "get_json"):
            result = orchestrator.run()
            return result

        payload = request.get_json(silent=True) or {}
        user_message = payload.get("message") or payload.get("prompt") or ""

        if user_message:
            result = orchestrator.run(user_message=user_message)
        else:
            result = orchestrator.run()

        return result, 200
    except Exception as exc:  # pragma: no cover
        return {"error": str(exc)}, 500