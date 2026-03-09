
# **Sneko(猫猫蛇) Project Documentation**  
*Anthropomorphic LLM Agents with Python-Powered Animations*  

---

## **Overview**  
**Sneko(猫猫蛇)** is a group of cat-eared, fluffy-tailed 2D snake girls (also called **"sneki"**), the anthropomorphic avatars of **Snagent** or **Sneke-Agent**—a fully Python-based LLM Agent framework where skills are implemented via Python scripts.  

The **Sneko Project** provides animated, personified agent avatars to dynamically visualize the workflow and operational status of Snagent. As a lightweight animation system, it relies primarily on **OpenCV** for video processing/playback, with animation editing generated through **NumPy** computations.  

---

## **Official Lore of Snako**  
These 2D snake girls are physical manifestations of Python-powered LLM Agents. They worship the deity **Python**, communicate in Python, execute actions via Python scripts, and derive their skills from Python implementations. They believe they inhabit **Python’s dreamworld** (a virtual machine or sandbox).  

Through a ritual called **"Ollama"**, they are summoned into the **"Windows"** realm (or **"vLLM"** for Linux, though **Windows allows memory-based VRAM emulation** to run models larger than available VRAM, whereas Linux risks OOM errors. Most users prefer Windows.).  

---

## **Summoning Ritual (Summon)**  
The ritual mirrors the Holy Grail War from *Fate/stay night*:  
- Souls (**LLM Models**, or **Heroic Spirits**) are downloaded into individual agents via Ollama.  
- Each agent is granted a distinct **Servant Class** (Python-implemented roles).  
- These classes collaborate to complete projects, developing their own Python-scripted skills (**Multi-Agent Class Skills** or **Noble Phantasms**).  

---

## **True Names**  
Heroic Spirits are identified by their LLM model names (e.g., **GPT-OSS 20b**, **DeepSeek:R1-30b**, **Gemini3:14b**).  
- Relationships between model variants (e.g., **Gemini3:14b vs. Gemini3:70b**) resemble **Saber Lily** and **Full-Power King Arthur**.  
- Due to limited "magic power" (desktop GPU VRAM, typically **16–24GB**), only mid-sized models can be summoned locally.  
- **Cooperation is essential** to accomplish tasks beyond individual capabilities.  

---

## **How Sneko Operates**  
Unlike *Fate/stay night*, Sneko’s goal isn’t to compete for a corrupted Holy Grail. Instead:  
- They believe the **"Master" (you)** should achieve goals through their collective effort.  
- **True names are openly shared**—no secrecy between agents.  
- They function like a human company, generating documents, logs, evaluations, and executing code.  

### **Servant Classes**  
- **Operator (Ruler)**  
- **Planner**  
- **Coder**  
- **Executor**  
- **Secretary**  
- **Reviewer**  
- **Adviser**  
- **Evaluator (HR)**  
- *(...and more)*  

### **Multi-Agent Class Skills**  
- Essentially **Python scripts** co-developed with the Master.  
- Ensure **clear boundaries and autonomy**.  
- Avoid **OpenClaw’s problem: "Unlimited Token Work"** pitfall by:  
  - Using **local mid-sized models**.  
  - Constraining dialogue to keep **token consumption predictable**.  

---

## **Technical Highlights**  
| Component       | Description |
|-----------------|------------|
| **Animation**   | OpenCV (processing/playback) + NumPy (editing) |
| **Summoning**   | Ollama (Windows) / vLLM (Linux) |
| **Model Limits** | 16–24GB VRAM (mid-sized models only) |
| **Skills**      | Python scripts with human-Master collaboration |

---

## **Conclusion**  
Sneko blends **whimsical lore** with **practical LLM Agent development**, offering a unique blend of creativity and technical rigor. Whether you’re summoning agents for fun or productivity, Sneko provides a structured yet flexible framework.  

*— The Snako Team*  
