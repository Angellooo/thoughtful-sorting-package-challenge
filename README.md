# Package Sorting Problem for Thoughtful AI 📦

This simple script implements and tests a function sort(width, height, length, mass) that classifies packages into categories based on their size and weight.

---

Problem Statement:

Packages must be dispatched into different stacks according to the following rules:

- **Bulky**:
  - A package is considered bulky if its **volume** (Width × Height × Length) is **≥ 1,000,000 cm³**,  
    **OR** if any single dimension is **≥ 150 cm**.
- **Heavy**:
  - A package is considered heavy if its **mass ≥ 20 kg**.

### Classification
- **STANDARD** → Package is **neither bulky nor heavy**.  
- **SPECIAL** → Package is **bulky OR heavy (but not both)**.  
- **REJECTED** → Package is **both bulky AND heavy**.

---

## 📝 Assumptions

1. **Thresholds are inclusive**:  
   - Volume exactly `1,000,000 cm³` counts as bulky.  
   - Dimension exactly `150 cm` counts as bulky.  
   - Mass exactly `20 kg` counts as heavy.  

2. **Inputs**:  
   - The `sort` function receives four arguments: `width`, `height`, `length` (in cm), and `mass` (in kg).  
   - All inputs are assumed to be positive numbers.  
   - Mass can be a floating‑point value.  

3. **Output**:  
   - The function returns one of the strings: `"STANDARD"`, `"SPECIAL"`, or `"REJECTED"`.  

---

## ✅ Test Coverage

The test suite (`test_cases.py`) covers:

- **Standard packages**  
  - Small, light packages that are neither bulky nor heavy.  

- **Bulky only**  
  - By volume (≥ 1,000,000 cm³).  
  - By dimension (≥ 150 cm).  
  - Edge cases at exactly the threshold.  

- **Heavy only**  
  - Mass exactly 20 kg.  
  - Mass greater than 20 kg.  

- **Rejected packages**  
  - Both bulky and heavy (volume + mass, or dimension + mass).  

- **Boundary conditions**  
  - Just below thresholds for volume, dimension, and mass.  

---

## 🧪 Running the script

Option 1: Clone the repository:
   ```bash
   git clone https://github.com/Angellooo/thoughtful-sort-package-challenge.git
   cd thoughtful-sorting-package-challenge

Option 2: Run the script directly in 
