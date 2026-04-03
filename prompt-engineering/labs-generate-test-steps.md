- **Lab: AI generated Test Steps for Jira User Stories**
    
    ## Step 1: Open Fresh Chat & Upload Documents
    
    **What to do:**
    
    - Open a **fresh chat** in Langdock
    - Select **Claude** as the LLM
    - Upload these **2 files:**
    
    | File | Why Upload This |
    | --- | --- |
    | `Test Input Summary — PVS-59215 & PVS-80605.docx` | Output from Part 1 — structured test inputs |
    | `Test Case - Filtering & Sorting with test data used.pdf` | Shows Claude the **exact format** of how RxLogix writes test cases |
    |  |  |
    
    ---
    
    ### ⚠️ Why Upload the Existing Test Case PDF Now?
    
    > In Part 1 we deliberately **excluded** this file to avoid bias during extraction.
    > 
    > 
    > In Part 2 we **include** it because we want Claude to **match the exact Jira test case format** RxLogix already follows — column names, structure, pass/fail format etc.
    > 
    
    ### Step 2: Writing the Context-Setting Prompt (Role / Persona Prompting)
    
    ---
    
    **What are we doing here?**
    
    Same as Part 1 Step 2 — we set the **role, context and ground rules** for Claude before asking it to do any real work.
    
    ---
    
    ### ✍️ The Context-Setting Prompt to Use
    
    Copy and paste this as your **first message** in the fresh chat:
    
    ---
    
    ```
    You are a Senior QA Analyst with deep expertise in pharmacovigilance software testing for RxLogix PV Signal application.
    
    You have been provided with 2 documents:
    
    1. Test Input Summary — PVS-59215 & PVS-80605
       - This contains all extracted field types, operators, business rules
         and edge cases for the Filtering & Sorting feature
       - This is your PRIMARY INPUT for generating test steps
    
    2. Existing Test Case Document — PVS-7.0-OQ-195
       - This contains real test cases already written by the RxLogix QA team
       - This is your REFERENCE for format, structure and writing style only
       - Do NOT reuse or copy any test steps from this document
    
    Your job is to generate new Jira test steps for the Filtering & Sorting
    feature based on the Test Input Summary.
    
    Ground Rules:
    - Generate test steps strictly based on Test Input Summary only
    - Follow the exact format and writing style of the existing test case document
    - Each test step must have: Step Number, Action, Expected Result
    - Be exhaustive — cover all field types, operators, rules and edge cases
    - Do NOT skip any scenario
    - If anything is unclear say "Not specified in the document"
    
    Acknowledge that you have read both documents and are ready to proceed.
    ```
    
    ---
    
    ### 🎓 Prompt Techniques Used Here
    
    | Technique | How It's Applied |
    | --- | --- |
    | **Role / Persona Prompting** | *"You are a Senior QA Analyst…"* |
    | **Contextual Prompting** | Clearly explaining what each uploaded document is for |
    | **Instructional Prompting** | Ground rules defined upfront |
    | **Clarification Prompting** | *"This is your PRIMARY INPUT… This is your REFERENCE… only"* |
    
    
    ## Step 3: The Test Step Generation Prompt
    
    ---
    
    **What are we doing here?**
    
    This is the **core prompt of Part 2.** We ask Claude to generate Jira test steps. But we will not ask it to generate everything at once — we will use **Few-Shot Prompting** to show Claude an example first, then ask it to generate.
    
    ---
    
    ### ✍️ The Test Step Generation Prompt to Use
    
    Copy and paste this as your **next message:**
    
    ---
    
    ```
    Now I will show you one example of how a test step should be written based on the RxLogix format.
    
    EXAMPLE:
    Step No: 1
    Action: Navigate to Alerts > Individual Case Review and open the alert.
            Click on the Product Name column header.
    Expected Result: The filtering and sorting menu is displayed with the
                     following options:
                     - Operator dropdown
                     - Filter text area
                     - Suggestion list
                     - Save, Reset Filter and Cancel buttons
    
    ---
    
    Now using this exact format, generate test steps for the following
    scenario ONLY:
    
    SCENARIO: Text Field Filtering
    - Cover all operators for Text field type
    - Cover the Save, Reset and Cancel button behaviors
    - Cover the Suggestion list behavior
    - Cover the No Matches edge case
    
    Rules:
    - Each step must be atomic — one action per step
    - Expected Result must be specific and measurable
    - Number the steps sequentially
    - Do not generate for any other field type yet
    ```
    
    ---
    
    ### 🎓 Prompt Techniques Used Here
    
    | Technique | How It's Applied |
    | --- | --- |
    | **Few-Shot Prompting** | Showing Claude one example before asking it to generate |
    | **Instructional Prompting** | *"Each step must be atomic — one action per step"* |
    | **Specific Example Prompt** | *"Cover all operators for Text field type"* |
    | **Formatting Prompt** | Exact format defined with Step No, Action, Expected Result |
    
    
    ## Step 4: Scaling to All Field Types using Prompt Chaining
    
    ---
    
    **What are we doing here?**
    
    In Step 3 we generated test steps for **Text Field only.** Now we scale it to **all remaining field types** one by one using Prompt Chaining. This demonstrates how to systematically scale AI output without losing quality.
    
    ---
    
    ### ✍️ The Scaling Prompt to Use
    
    Copy and paste this as your **next message:**
    
    ---
    
    ```
    The test steps for Text Field look good.
    
    Now using the exact same format and quality, generate test steps
    for the remaining field types one by one in this order:
    
    1. Number Field
       - Cover all operators (Between, Equals, Greater Than, Less Than etc.)
       - Cover From and To behavior for Between operator
       - Cover No Matches edge case
       - Cover negative values for Due In field
    
    2. Date Field
       - Cover all operators (Equals, Between, Last X Days, Next X Months etc.)
       - Cover date picker behavior
       - Cover From and To behavior for Between operator
       - Cover Last X logic (date picker converts to number input)
       - Cover future date operators — only available for fields that support future dates
    
    3. Stacked Columns
       - Cover separate filtering per sub-column
       - Cover separate sorting per sub-column
    
    4. Special Fields (Comment, Attachment, Action Item)
       - Cover Is Empty and Is Not Empty behavior
       - Cover sorting order for each
    
    5. Large Text Fields
       - Cover no suggestion list behavior
       - Cover filtering still works via text input
    
    Generate field type by field type — wait for my confirmation
    before moving to the next field type.
    ```
    
    ---
    
    ### 🎓 Prompt Techniques Used Here
    
    | Technique | How It's Applied |
    | --- | --- |
    | **Prompt Chaining** | *"The test steps for Text Field look good — now continue…"* |
    | **Instructional Prompting** | Ordered list of field types with specific coverage points |
    | **Clarification Prompting** | *"Wait for my confirmation before moving to next field type"* |
    | **Specific Example Prompt** | Specific behaviors called out for each field type |
    
    
    ---
    
    ### ✍️ The Final Prompt to Use
    
    ```
    All field types are now covered and confirmed.
    
    Now consolidate all the generated test steps into one final
    complete test case document with the following structure:
    
    HEADER:
    - Test Script No: PVS-7.0-OQ-[Next Number]
    - Test Case Name: Usability Enhancements — Filtering & Sorting
    - Test Objective: [Generate based on PVS-59215 and PVS-80605]
    - Requirements Reference: PVS-59215, PVS-80605
    - Acceptance Criteria: All test steps pass successfully
    
    TEST STEPS TABLE:
    Columns:
    - Step No
    - Action
    - Expected Result
    - Actual Result (leave blank)
    - Pass / Fail (leave blank)
    - Verified By (leave blank)
    
    At the end add a COVERAGE SUMMARY:
    - Total Test Steps Generated
    - Field Types Covered
    - Operators Covered
    - Business Rules Covered
    - Edge Cases Covered
    
    Save this as a Word document titled:
    "PVS-7.0-OQ-[Next Number] — Filtering & Sorting Test Case"
    ```
    
    ---
    
    ### 🎓 Prompt Techniques Used Here
    
    | Technique | How It's Applied |
    | --- | --- |
    | **Prompt Chaining** | *"All field types are now covered and confirmed — consolidate…"* |
    | **Formatting Prompt** | Exact table columns matching RxLogix format |
    | **Instructional Prompting** | Header fields, table structure and coverage summary defined |
    
    ---