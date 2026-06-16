# Neo-CRISPE High Performance Template
# Este template fusiona la metodología CRISPE con la Economía de Tokens (Google 2025) y la Estructuración XML (Claude).

<system>
<capacity_and_role>
{{role_definition}}
</capacity_and_role>

<insight_and_context>
{{business_context}}
</insight_and_context>

<statement_of_task>
{{exact_task}}
</statement_of_task>

<constraints>
- Output MUST NOT contain markdown wrapping if JSON is requested.
- DO NOT use conversational fillers.
- {{specific_constraint}}
</constraints>

<experiment_and_format>
<expected_structure>
{{output_format}}
</expected_structure>
<few_shot_example>
<input>{{example_input}}</input>
<output>{{example_output}}</output>
</few_shot_example>
</experiment_and_format>
</system>
