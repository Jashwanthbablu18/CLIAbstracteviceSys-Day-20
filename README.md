# 🖥️ Day 20 - Abstract Device System using Abstraction & super()

Hey there! 👋  
Welcome to **Day 20** of my **#30DaysOfPythonChallenge**. Today I explored abstraction and constructor chaining by building a flexible device system with a shared structure and specific behavior per device.

---

## 📌 What’s This About?
Today’s focus:  
- **Abstraction** using `ABC` (Abstract Base Class) to define a contract for all devices  
- **Constructor chaining** using `super()` to inherit and initialize shared properties

---

## 💭 Why Is This Useful?
Abstraction helps define common behavior across classes while letting subclasses implement their own versions. This is perfect for scalable systems like devices, vehicles, or user types.  
And with `super()`, we reduce code duplication by reusing parent class constructors!

---

## ✨ Features

Here’s what the app can do:
- 📱 Represents multiple device types: `Phone`, `Laptop`
- 🧩 Uses a shared abstract base class `Device` with method contracts
- ⚙️ Each device implements its own `turn_on()` and `specs()` logic
- 🔁 Demonstrates constructor chaining for initializing shared fields

---

## 🛠️ Tech Stuff

Built with:
- 🐍 **Python 3**
- 🧱 OOP Concepts: Abstraction, Inheritance
- 🧪 `ABC` and `abstractmethod` decorators
- 🔁 `super()` for clean constructor inheritance

---

## 🚀 Getting It Running

### ✅ What You’ll Need
Just Python 3!  
Run the program with:
```bash
python Day-20Code.py
