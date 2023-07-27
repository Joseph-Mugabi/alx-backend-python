# ***Unittests and Integration Tests***
|## 1. ~Unit Tests:~ | *Integration Tests*|
|--------------------|--------------------|
|```
Unit tests are a type of testing that focuses on validating the smallest
 testable components of a software system in isolation. These components,
  called "units," can be individual functions, methods, or classes. 
  The goal of unit testing is to ensure that each unit of code functions 
  correctly and produces the expected output for various input scenarios. 
  Unit tests are typically written by developers during the coding phase 
  of software development.|Integration tests, on the other hand, verify 
  the interactions and behavior of multiple components or modules within 
  a software system. Unlike unit tests, integration tests aim to test how
 various components work together as a whole, simulating the interactions 
 they would have in a real-world scenario. Integration testing ensures 
 that different parts of the software can integrate seamlessly and 
 function correctly together.```|

 `
 #!/usr/bin/env python3

import requests
import json

response = requests.get("https://api.github.com/orgs/abc")
print(response.json())
`
