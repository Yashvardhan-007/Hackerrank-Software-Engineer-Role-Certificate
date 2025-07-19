# Hackerrank-Software-Engineer-Role-Certificate

PROBLEM 1-
# 🌱 Growth in 2D Grid

## 📌 Problem Statement

You are given a list of coordinate pairs, each representing the top-right corner `(r, c)` of a subgrid starting from (1,1).  
Each operation increases the count of every cell in the subgrid by **1**.

Your task is to return the number of cells in the grid that contain the **maximum value** after all operations are applied.

---

## 🧠 Intuition

The cell(s) that are included in **all** operations will have the **maximum** value, as they are incremented the most.

To find those cells:
- Take the **minimum** row and column values across all operations.
- The overlapping subgrid is from (1,1) to `(min_r, min_c)`.
- Hence, the number of such max-value cells is:  
  `min_r × min_c`

---

## ✅ Input Format

- A list of strings `["r1 c1", "r2 c2", ..., "rn cn"]` where each element is a coordinate pair.

PROBLEM 2-
# 🧾 Largest Number of Orders

## 📌 Problem Statement

You are given a table named `ORDERS` with the following structure:

| Column Name  | Data Type | Description              |
|--------------|-----------|--------------------------|
| ID           | INT       | Order ID (Primary Key)   |
| ORDER_DATE   | DATE      | Date of the order        |
| STATUS       | VARCHAR   | Status of the order      |
| CUSTOMER_ID  | INT       | ID of the customer       |

Your task is to find the `CUSTOMER_ID` who placed the **highest number of orders**.  
If multiple customers are tied with the same number of orders, return the one with the **smallest CUSTOMER_ID**.

---

## 🎯 Requirements

- Output only **one** row.
- Use **aggregate functions** and sorting.
- Assume standard SQL behavior with **MySQL**.

---

PROBLEM 3-
# MedicalRecordTemperature

This repository contains a Python script to calculate the average body temperature for a patient from a paginated REST API.

## Description
The script fetches medical records for a given user ID from a mock REST API[](https://jsonmock.hackerrank.com/api/medical_records) and computes the average body temperature based on the `vitals.bodyTemperature` field. It handles pagination and returns "0" if no records are found.

## Features
- Fetches data from a paginated REST API.
- Calculates the average body temperature with one decimal place.
- Handles empty result sets by returning "0".

## Requirements
- Python 3.x
- `requests` library (install via `pip install requests`)

