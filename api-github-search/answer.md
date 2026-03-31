# Answers

## 1. What is the role of query parameters in this request?

Query parameters are used to customize and control the API request.  
In this case:

- `q=python` → searches for repositories related to Python  
- `sort=stars` → sorts repositories based on star count  
- `order=desc` → arranges results in descending order  
- `per_page=5` → limits the output to only 5 repositories  

They allow us to filter, sort, and limit the data returned by the API.

---

## 2. Why do we use response.json() instead of response.text?

- `response.json()` converts the API response into a Python dictionary  
- It allows easy access to data using keys (like `data["items"]`)  

On the other hand:

- `response.text` returns raw text (string format)  
- It is harder to extract structured data from it  

So, `response.json()` is preferred because it makes data handling easier and more efficient.