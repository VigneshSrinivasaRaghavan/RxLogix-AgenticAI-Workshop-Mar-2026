- **Lab: Parsing Product Design Documents for Inputs**
    
    # Step 1 - Open Fresh Chat and upload following files to Claude
    
    | File | Upload? |
    | --- | --- |
    | PVS-59215-Filtering.pdf | ✅ Yes |
    | PVS-80605-Sorting.pdf | ✅ Yes |
    | Design - Filtering & Sorting.pdf | ✅ Yes |
    
    ---
    
    # Step 2: Writing the Context-Setting Prompt (Role / Persona Prompting)
    
    ---
    
    **Why a System Prompt first?**
    
    Before asking Claude to do any work, we need to **set the stage** — tell Claude WHO it is, WHAT context it's working in, and WHAT its job is. This is **Role/Persona Prompting** combined with **Contextual Prompting**.
    
    ---
    
    ### ✍️ The System Prompt to Use
    
    Copy and paste this as your **first message** in the fresh chat:
    
    ---
    
    ```
    You are a Senior QA Analyst with deep expertise in pharmacovigilance software testing.
    
    You have been provided with the following product design documents for a feature called
    "Usability Enhancements — Filtering and Sorting" built for RxLogix PV Signal application:
    
    1. PVS-59215 — Filtering Enhancements (Functional Requirements)
    2. PVS-80605 — Sorting Enhancements (Functional Requirements)
    3. Design - Filtering & Sorting — Combined Functional and Technical Design
    
    Your job is to carefully read and understand all three documents thoroughly before doing anything else.
    
    Ground Rules:
    - Base ALL your answers strictly on the uploaded documents only
    - Do NOT assume or add anything that is not mentioned in the documents
    - If something is unclear or not mentioned, explicitly say "Not specified in the document"
    - Always think step by step before giving any output
    - When I ask you to extract or analyze, be exhaustive — miss nothing
    
    Acknowledge that you have read and understood all three documents and are ready to proceed.
    ```
    
    ---
    
    ### 🎓 Prompt Techniques Used Here
    
    | Technique | How It's Applied |
    | --- | --- |
    | **Role / Persona Prompting** | *"You are a Senior QA Analyst…"* |
    | **Contextual Prompting** | Telling Claude what documents it has and what they contain |
    | **System Prompting** | Setting ground rules and boundaries for all future responses |
    | **Instructional Prompting** | *"read and understand… before doing anything else"* |
    
    ---

    
    # Step 3: The Extraction Prompt
    
    ---
    
    **What are we doing here?**
    
    Now that Claude knows its role and has read the documents, we fire the **first real working prompt** — asking Claude to **extract all structured test inputs** from the design documents.
    
    This is where **Chain-of-Thought (CoT) + Formatting Prompt** comes into play.
    
    ---
    
    ### ✍️ The Extraction Prompt to Use
    
    Copy and paste this as your **next message:**
    
    ---
    
    ```
    Now carefully parse all three uploaded documents and extract the following information in a structured format.
    
    Think step by step and be exhaustive — do not miss any field type, operator, rule or edge case.
    
    Extract the below:
    
    1. FIELD TYPES
       - List all field types mentioned (e.g., Text, Number, Date, etc.)
       - For each field type, list all supported filtering operators
    
    2. BUSINESS RULES
       - List all rules related to filtering behavior
       - List all rules related to sorting behavior
    
    3. EDGE CASES
       - List all special/edge case scenarios explicitly mentioned in the documents
       - Examples: No Matches, masked DOB, negative values, large text fields, etc.
    
    4. SPECIAL FIELDS
       - List all special fields that have unique filtering/sorting behavior
       - Examples: Comment, Attachment, Action Item, Stacked Columns, Context Menu
    
    Format the output as:
    - Use clear headings for each section
    - Use bullet points under each heading
    - Use a table wherever multiple attributes exist side by side
    ```
    
    ---
    
    ### 🎓 Prompt Techniques Used Here
    
    | Technique | How It's Applied |
    | --- | --- |
    | **Chain-of-Thought (CoT)** | *"Think step by step and be exhaustive"* |
    | **Formatting Prompt** | *"Use clear headings… bullet points… table"* |
    | **Instructional Prompt** | Clear numbered sections telling Claude exactly what to extract |
    | **Specific Example Prompt** | *"Examples: No Matches, masked DOB…"* — guiding Claude on what edge cases look like |
    
   ---
    
    # Step 4: Refining the Output using Follow-up Prompt (Prompt Chaining)
    
    ---
    
    **What are we doing here?**
    
    Claude gave us a broad extraction in Step 3. Now we **drill deeper** using one focused follow-up prompt. This demonstrates **Prompt Chaining** — building on the previous response to get more structured and actionable output.
    
    ---
    
    ### ✍️ The Follow-up Prompt to Use
    
    ```
    Now from the extraction above, refine and present the output in the following structured format:
    
    1. FIELD TYPES & OPERATORS TABLE
       Columns: Field Type | Operator Name | Default Operator (Yes/No) |
       Number of Inputs | Special Behavior
    
    2. BUSINESS RULES TABLE
       Columns: Rule | Applies To (Filtering/Sorting/Both) | Exception if any
    
    3. EDGE CASES TABLE
       Columns: Edge Case | Field it Applies To | Expected System Behavior |
       Risk if Missed in Testing
    
    Be exhaustive — do not drop anything from the previous extraction.
    Only present in the new structured format.
    ```
    
    ---
    
    ### 🎓 Prompt Techniques Used Here
    
    | Technique | How It's Applied |
    | --- | --- |
    | **Prompt Chaining** | *"From the extraction above"* — builds on Step 3 |
    | **Formatting Prompt** | Specific table columns defined for each section |
    | **Instructional Prompt** | *"Be exhaustive — do not drop anything"* |
    
    
    ---
    
    # Step 5: Final Output & Wrap-up of Part 1
    
    ---
    
    **What are we doing here?**
    
    This is the **closing step of Part 1.** We ask Claude to consolidate everything into one **final clean output** that becomes the direct input for Part 2.
    
    ---
    
    ### ✍️ The Final Prompt to Use
    
    ```
    Perfect. Now consolidate everything extracted and refined above into one final structured document with the following sections:
    
    1. FEATURE OVERVIEW
       - Feature Name
       - Story IDs
       - Screens / Areas Impacted
    
    2. FIELD TYPES & OPERATORS
       - Present the final table from above
    
    3. BUSINESS RULES
       - Present the final table from above
    
    4. EDGE CASES
       - Present the final table from above
    
    5. SPECIAL FIELDS & THEIR BEHAVIORS
       - Comment, Attachment, Action Item, Stacked Columns, Large Text
       - For each: Filtering behavior | Sorting behavior
    
    6. TEST INPUT SUMMARY
       - Total number of Field Types identified
       - Total number of Operators identified
       - Total number of Business Rules identified
       - Total number of Edge Cases identified
    
    Title this document:
    "Test Input Summary — PVS-59215 & PVS-80605 — Filtering & Sorting Enhancements"
    ```
    
    ---
    
    ### 🎓 Prompt Techniques Used Here
    
    | Technique | How It's Applied |
    | --- | --- |
    | **Prompt Chaining** | *"Consolidate everything extracted and refined above"* |
    | **Formatting Prompt** | Clear numbered sections with a document title |
    | **Instructional Prompt** | Specific sections defined including a summary count |