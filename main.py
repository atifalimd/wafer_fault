from flask import Flask, request, render_template, Response
import os
from flask_cors import CORS, cross_origin
import json


def training_route():
    path = "Dataset"
    train_val = train_validation(path)

training_route()
    