### **Agile Methodology**
* Agile is an iterative and incremental software development methodology that focuses on collaboration, customer feedback, flexibility, and continuous delivery of working software.
* Agile ek software development approach hai jisme project ko chhote-chhote parts (iterations / sprints) me develop kiya jata hai aur customer se regular feedback lekar continuously improvements ki jati hain.

#### Benefits of Agile
* Faster delivery
* Better customer satisfaction
* Easy to handle changing requirements
* Continuous feedback
* Reduced project risk
* Better team collaboration

### What are Agile principles?
* Agile principles are 12 guidelines defined in the Agile Manifesto. They focus on customer satisfaction, frequent delivery of working software, accepting changing requirements, collaboration, continuous improvement, technical excellence, and empowering self-organizing teams.
* Agile principles are 12 guidelines from the Agile Manifesto that help teams develop software flexibly, collaboratively, and with continuous customer feedback.
| #   | Principle                         | Simple Meaning                                                     |
| --- | --------------------------------- | ------------------------------------------------------------------ |
| 1   | **Customer satisfaction**         | Deliver valuable software early and continuously.                  |
| 2   | **Welcome changing requirements** | Accept changes, even late in development.                          |
| 3   | **Frequent delivery**             | Deliver working software frequently in small increments.           |
| 4   | **Daily collaboration**           | Business and development teams should work together regularly.     |
| 5   | **Trust the team**                | Give motivated team members the support and environment they need. |
| 6   | **Face-to-face communication**    | Direct communication is highly effective for sharing information.  |
| 7   | **Working software**              | Working software is the primary measure of progress.               |
| 8   | **Sustainable development**       | Maintain a sustainable pace that can continue long-term.           |
| 9   | **Technical excellence**          | Continuously improve technical quality and good design.            |
| 10  | **Keep it simple**                | Avoid unnecessary work and focus on what provides value.           |
| 11  | **Self-organizing teams**         | Teams should organize themselves to find effective ways to work.   |
| 12  | **Continuous improvement**        | Regularly reflect on how to improve and adjust accordingly.        |
```
Customer
   ↓
Change
   ↓
Frequent Delivery
   ↓
Collaboration
   ↓
Trust Team
   ↓
Communication
   ↓
Working Software
   ↓
Sustainable Pace
   ↓
Technical Excellence
   ↓
Simplicity
   ↓
Self-Organizing Team
   ↓
Continuous Improvement
```

### Agile Roles?
1. Product Owner (PO)
   1. Represents customer/business
   2. Defines requirements
   3. Prioritizes backlog
2. Scrum Master
   1. Facilitates Agile process
   2. Removes blockers
   3. Ensures Scrum practices are followed
3. Development Team
   1. Developers
   2. Testers
   3. DevOps Engineers
   4. Business Analysts

### ⭐ **Agile Ceremonies?**
1. Sprint Planning
   1. Sprint start me decide karte hain ki kya develop karna hai.
2. Daily Standup
   1. 15-minute daily meeting.
   2. Questions:
      1. What did I do yesterday?
      2. What will I do today?
      3. Any blockers?
3. Sprint Review
   1. Team completed work demo karti hai.
4. Sprint Retrospective
   1. Team discuss karti hai:
      1. What went well?
      2. What can be improved?

### **What is Waterfall Methodology?**
* Waterfall is a **linear and sequential software development methodology** where the **project is completed phase by phase. The next phase starts only after the previous phase is completed**.
* Waterfall is a **sequential software development methodology** in which each phase is completed before moving to the next phase.
* Waterfall = Complete one phase → then move to the next phase.
```bash
Requirements
     ↓
Design
     ↓
Development
     ↓
Testing
     ↓
Deployment
     ↓
Maintenance
```

#### Example
* Suppose we are developing an **Employee Management System**:
  * **Requirements** → Gather all requirements
  * **Design** → Design database and application architecture
  * **Development** → Write the code
  * **Testing** → Test the complete application
  * **Deployment** → Release to production
  * **Maintenance** → Fix bugs and maintain the system


### Difference between Agile and Waterfall?
* **Agile** is an iterative development methodology where software is developed and delivered in small increments with continuous feedback and flexibility for changing requirements. **Waterfall** is a sequential methodology where requirements, design, development, testing, and deployment are completed phase by phase.
* The main difference is that Waterfall follows a sequential approach, while Agile follows an iterative and incremental approach.
* **HINDI:-**
* Waterfall में पूरा project एक fixed sequence में phase-by-phase चलता है, जबकि Agile में project को छोटे-छोटे Sprints में divide करके बार-बार develop, test और improve किया जाता है।

| Point                    | Agile                                 | Waterfall                                    |
| ------------------------ | ------------------------------------- | -------------------------------------------- |
| **Approach**             | Iterative & incremental               | Sequential                                   |
| **Requirements**         | Can change during development         | Usually defined upfront(शुरुआत में mostly fixed) |
| **Development**          | Done in small iterations/Sprints      | Done phase by phase                          |
| **Testing**              | Continuous throughout development     | Usually after development                    |
| **Customer Feedback**    | Frequent                              | Usually at specific milestones               |
| **Delivery**             | Frequent/incremental                  | Usually at the end                           |
| **Changes**              | Easier to accommodate                 | Can be difficult and costly later            |
| **Customer Involvement** | High                                  | Comparatively lower                          |
| **Risk**                 | Identified earlier through iterations | Can be discovered later                      |
| **Best suited for**      | Changing/uncertain requirements       | Stable and well-defined requirements         |

```bash
# Example
-> Waterfall: You generally complete one phase before moving to the next.

   Requirements
      ↓
   Design
      ↓
   Development
      ↓
   Testing
      ↓
   Deployment


-> Agile: Each Sprint produces a working increment and allows feedback.

Sprint 1 → Login
Sprint 2 → Registration
Sprint 3 → Profile
Sprint 4 → Reports
```




### **What is a Sprint?**
* A Sprint is a fixed time period (usually 1–4 weeks) during which a team develops and delivers a set of features.
```bash
# Example
Sprint 1 → Login Module
Sprint 2 → User Dashboard
Sprint 3 → Reports Module
```

### What is Sprint Review?
* At the end of every two-week Sprint, I participate in the Sprint Review where we demonstrate the completed features to the Product Owner and stakeholders. We collect their feedback and update the Product Backlog based on the requirements.
* Sprint Review is a meeting held at the end of a Sprint to demonstrate the completed work to stakeholders, gather feedback, and discuss what should be done next.
* **Example:-**
  * Suppose your Sprint is 2 weeks and the team worked on a Login Module.

```bash
# During Sprint Review:
Development Team
       ↓
Demonstrates Login Module
       ↓
Product Owner / Stakeholders
       ↓
Feedback
       ↓
Future Backlog Updates
```
* For example, stakeholders may say:
  * "Login is working, but we also need Google Login."

#### Who participates?
* Product Owner
* Scrum Master
* Developers / Scrum Team
* Stakeholders (when appropriate)

#### Sprint Review vs Sprint Retrospective
| Sprint Review               | Sprint Retrospective               |
| --------------------------- | ---------------------------------- |
| Focuses on **product/work** | Focuses on **team/process**        |
| Demonstrate completed work  | Discuss how the team worked        |
| Stakeholder feedback        | Team improvement                   |
| What did we build?          | What went well / what can improve? |
| Usually at Sprint end       | After Sprint Review                |


### **What is Sprint Backlog?**
* Sprint Backlog is the list of Product Backlog items selected for the current Sprint, along with the plan/tasks needed to deliver them.
* Sprint Backlog is a list of user stories, requirements, and tasks that the Scrum Team commits to work on during a particular Sprint.
* Sprint Backlog is the subset of the Product Backlog selected for a particular Sprint. It contains the user stories and tasks that the development team plans to complete during that Sprint.
* Example
```bash
Suppose the Product Backlog contains:

1. User Registration
2. Login
3. Forgot Password
4. User Profile
5. Payment
6. Reports

For a 2-week Sprint, the team selects:

Sprint Backlog
-------------------------
1. User Registration
2. Login
3. Forgot Password

These can then be broken into development tasks:

Login
 ├── Create API
 ├── Create database query
 ├── Implement validation
 ├── Write unit tests
 └── Code review
```

### Product Backlog vs Sprint Backlog
| Product Backlog                      | Sprint Backlog                               |
| ------------------------------------ | -------------------------------------------- |
| Contains all planned work            | Contains work selected for current Sprint    |
| Managed/prioritized by Product Owner | Created and managed by Scrum Team            |
| Can contain future requirements      | Focuses on current Sprint                    |
| Changes continuously                 | Changes as the Sprint progresses when needed |
* Easy way to remember
  * **Product Backlog** = What could we build?
  * **Sprint Backlog** = What are we working on in this Sprint?

### What is Sprint Retrospective?
* Sprint Retrospective is a Scrum meeting held after the Sprint where the Scrum Team discusses how the Sprint went, what went well, what problems occurred, and how the team can improve in the next Sprint.
* **Sprint Retrospective is a meeting** held at the end of a Sprint where the team reflects on its process, identifies improvements, and creates an action plan for the next Sprint.
```bash
Example

Suppose your team completed a 2-week Sprint.

During the Retrospective, the team discusses:

What went well?

Development was completed on time.
Good communication between developers and testers.

What didn't go well?

Requirements were unclear.
Code review took too long.
Some bugs were found late.

What can we improve?

Clarify requirements before starting development.
Do code reviews earlier.
Increase unit test coverage.
Sprint Completed
       ↓
Retrospective
       ↓
What went well?
       ↓
What didn't go well?
       ↓
What can we improve?
       ↓
Action items for next Sprint
Sprint Review vs Retrospective
Sprint Review	Sprint Retrospective
Focuses on product	Focuses on process/team
Demonstrate completed work	Discuss how the Sprint went
Stakeholder feedback	Team feedback
"What did we build?"	"How can we work better?"
Interview Answer

At the end of each Sprint, we conduct a Sprint Retrospective to discuss what went well, what went wrong, and what improvements we can make in the next Sprint. We then define action items and try to implement them in the upcoming Sprint.
```

### What is Daily Standup?
* Daily Standup (or Daily Scrum) is a **short daily meeting**, usually **around 15 minutes**, where the Scrum Team discusses progress, plans for the day, and any blockers.
* Daily Standup is a short daily meeting where team members share their progress, today's plan, and any blockers that may affect their work.

#### Three Common Questions
* Each team member typically answers:
  * What did I do yesterday?
  * What will I do today?
  * Do I have any blockers or issues?

