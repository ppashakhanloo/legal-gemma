# This function takes on row from the dataset and prepares a context, a question, and answer depending on the task type.
# All the strings in this transformation are grabbed from the provided dataset.
def transform_data(row):
    if row.task in ['abercrombie']:
        context = 'A mark is generic if it is the common name for the product. A mark is descriptive if it describes a purpose, nature, or attribute of the product. A mark is suggestive if it suggests or implies a quality or characteristic of the product. A mark is arbitrary if it is a real English word that has no relation to the product. A mark is fanciful if it is an invented word.'
        question = row.inputs['text'].replace('The mark ', 'What is the mark ')[:-1] + '?'
        answer = row.answer
    elif row.task in ['canada_tax_court_outcomes']:
        context = row.inputs['text']
        question = 'Indicate whether the following judgment excerpt from a Tax Court of Canada decision allows the appeal or dismisses the appeal. Where the result is mixed, indicate that the appeal was allowed. Ignore costs orders. Where the outcome is unclear indicate other.'
        answer = row.answer
    elif row.task in ['citation_prediction_classification']:
        context = row.inputs['text']
        question = 'Can the case be used as a citation for the provided text?'
        answer = row.answer
    elif row.task in ['citation_prediction_open']:
        context = row.inputs['text']
        question = 'Generate the best citation for the following texts, imagining you are in the following circuit: ' + row.inputs['circuit'] + '.'
        answer = row.answer
    elif row.task in ['consumer_contracts_qa']:
        context = row.inputs['contract']
        question = row.inputs['question']
        answer = row.answer
    elif row.task in ['contract_nli_confidentiality_of_agreement']:
        context = row.inputs['text']
        question = 'Identify if the clause provides that the Receiving Party shall not disclose the fact that Agreement was agreed or negotiated.'
        answer = row.answer
    elif row.task in ['contract_nli_explicit_identification']:
        context = row.inputs['text']
        question = 'Identify if the clause provides that all Confidential Information shall be expressly identified by the Disclosing Party.'
        answer = row.answer
    elif row.task in ['contract_nli_inclusion_of_verbally_conveyed_information']:
        context = row.inputs['text']
        question = 'Identify if the clause provides that Confidential Information may include verbally conveyed information.'
        answer = row.answer
    elif row.task in ['contract_nli_limited_use']:
        context = row.inputs['text']
        question = 'Identify if the clause provides that the Receiving Party shall not use any Confidential Information for any purpose other than the purposes stated in Agreement.'
        answer = row.answer
    elif row.task in ['contract_nli_no_licensing']:
        context = row.inputs['text']
        question = 'Identify if the clause provides that the Agreement shall not grant Receiving Party any right to Confidential Information.'
        answer = row.answer
    elif row.task in ['contract_nli_notice_on_compelled_disclosure']:
        context = row.inputs['text']
        question = 'Identify if the clause provides that the Receiving Party shall notify Disclosing Party in case Receiving Party is required by law, regulation or judicial process to disclose any Confidential Information.'
        answer = row.answer
    elif row.task in ['contract_nli_permissible_acquirement_of_similar_information']:
        context = row.inputs['text']
        question = 'Identify if the clause provides that the Receiving Party may acquire information similar to Confidential Information from a third party.'
        answer = row.answer
    elif row.task in ['contract_nli_permissible_copy']:
        context = row.inputs['text']
        question = 'Identify if the clause provides that the Receiving Party may create a copy of some Confidential Information in some circumstances.'
        answer = row.answer
    elif row.task in ['contract_nli_permissible_development_of_similar_information']:
        context = row.inputs['text']
        question = 'Identify if the clause provides that the Receiving Party may independently develop information similar to Confidential Information.'
        answer = row.answer
    elif row.task in ['contract_nli_permissible_post-agreement_possession']:
        context = row.inputs['text']
        question = 'Identify if the clause provides that the Receiving Party may retain some Confidential Information even after the return or destruction of Confidential Information.'
        answer = row.answer
    elif row.task in ['contract_nli_return_of_confidential_information']:
        context = row.inputs['text']
        question = 'Identify if the clause provides that the Receiving Party shall destroy or return some Confidential Information upon the termination of Agreement.'
        answer = row.answer
    elif row.task in ['contract_nli_sharing_with_employees']:
        context = row.inputs['text']
        question = 'Identify if the clause provides that the Receiving Party may share some Confidential Information with some of Receiving Party\'s employees.'
        answer = row.answer
    elif row.task in ['contract_nli_sharing_with_third-parties']:
        context = row.inputs['text']
        question = 'Identify if the clause provides that the Receiving Party may share some Confidential Information with some third-parties (including consultants, agents and professional advisors).'
        answer = row.answer
    elif row.task in ['contract_nli_survival_of_obligations']:
        context = row.inputs['text']
        question = 'Identify if the clause provides that ome obligations of Agreement may survive termination of Agreement.'
        answer = row.answer
    elif row.task in ['contract_qa']:
        context = row.inputs['text']
        question = row.inputs['question']
        answer = row.answer
    elif row.task in ['corporate_lobbying']:
        context = 'Official title of bill: ' + row.inputs['bill_title'] + '\n' + 'Official summary of bill: ' + row.inputs['bill_summary'] + '\n' + 'Company name: ' + row.inputs['company_name'] + '\n' + 'Company business description: ' + row.inputs['company_description']
        question = 'You are a lobbyist analyzing Congressional bills for their impacts on companies. Given the title and summary of the bill, plus information on the company from its 10K SEC filing, it is your job to determine if a bill is at least somewhat relevant to a company in terms of whether it could impact the company\'s bottom-line if it was enacted. ' + 'Is this bill potentially relevant to the company?'
        answer = row.answer
    elif row.task in ['cuad_affiliate_license-licensee']:
        context = row.inputs['text']
        question = 'Does the clause describe a license grant to a licensee (incl. sublicensor) and the affiliates of such licensee/sublicensor?'
        answer = row.answer
    elif row.task in ['cuad_affiliate_license-licensor']:
        context = row.inputs['text']
        question = 'Does the clause describe a license grant by affiliates of the licensor or that includes intellectual property of affiliates of the licensor?'
        answer = row.answer
    elif row.task in ['cuad_anti-assignment']:
        context = row.inputs['text']
        question = 'Does the clause require consent or notice of a party if the contract is assigned to a third party?'
        answer = row.answer
    elif row.task in ['cuad_audit_rights']:
        context = row.inputs['text']
        question = 'Does the clause give a party the right to audit the books, records, or physical locations of the counterparty to ensure compliance with the contract?'
        answer = row.answer
    elif row.task in ['cuad_cap_on_liability']:
        context = row.inputs['text']
        question = 'Does the clause specify a cap on liability upon the breach of a party’s obligation? This includes time limitation for the counterparty to bring claims or maximum amount for recovery.'
        answer = row.answer
    elif row.task in ['cuad_change_of_control']:
        context = row.inputs['text']
        question = 'Does the clause give one party the right to terminate or is consent or notice required of the counterparty if such party undergoes a change of control, such as a merger, stock sale, transfer of all or substantially all of its assets or business, or assignment by operation of law?'
        answer = row.answer
    elif row.task in ['cuad_competitive_restriction_exception']:
        context = row.inputs['text']
        question = 'Does the clause mention exceptions or carveouts to Non-Compete, Exclusivity and No-Solicit of Customers?'
        answer = row.answer
    elif row.task in ['cuad_covenant_not_to_sue']:
        context = row.inputs['text']
        question = 'Is a party restricted from contesting the validity of the counterparty’s ownership of intellectual property or otherwise bringing a claim against the counterparty for matters unrelated to the contract?'
        answer = row.answer
    elif row.task in ['cuad_effective_date']:
        context = row.inputs['text']
        question = 'Does the clause specify the date upon which the agreement becomes effective?'
        answer = row.answer
    elif row.task in ['cuad_exclusivity']:
        context = row.inputs['text']
        question = 'Does the clause specify exclusive dealing commitment with the counterparty? This includes a commitment to procure all “requirements” from one party of certain technology, goods, or services or a prohibition on licensing or selling technology, goods or services to third parties, or a prohibition on collaborating or working with other parties), whether during the contract or after the contract ends (or both).'
        answer = row.answer
    elif row.task in ['cuad_expiration_date']:
        context = row.inputs['text']
        question = 'Does the clause specify the date upon which the initial term expires?'
        answer = row.answer
    elif row.task in ['cuad_governing_law']:
        context = row.inputs['text']
        question = 'Does the clause specify which state/country\'s law governs the contract?'
        answer = row.answer
    elif row.task in ['cuad_insurance']:
        context = row.inputs['text']
        question = 'Is there a requirement for insurance that must be maintained by one party for the benefit of the counterparty?'
        answer = row.answer
    elif row.task in ['cuad_ip_ownership_assignment']:
        context = row.inputs['text']
        question = 'Does intellectual property created by one party become the property of the counterparty, either per the terms of the contract or upon the occurrence of certain events?'
        answer = row.answer
    elif row.task in ['cuad_irrevocable_or_perpetual_license']:
        context = row.inputs['text']
        question = 'Does the clause specify a license grant that is irrevocable or perpetual?'
        answer = row.answer
    elif row.task in ['cuad_joint_ip_ownership']:
        context = row.inputs['text']
        question = 'Does the clause provide for joint or shared ownership of intellectual property between the parties to the contract?'
        answer = row.answer
    elif row.task in ['cuad_license_grant']:
        context = row.inputs['text']
        question = 'Does the clause contain a license granted by one party to its counterparty?'
        answer = row.answer
    elif row.task in ['cuad_liquidated_damages']:
        context = row.inputs['text']
        question = 'Does the clause award either party liquidated damages for breach or a fee upon the termination of a contract (termination fee)?'
        answer = row.answer
    elif row.task in ['cuad_minimum_commitment']:
        context = row.inputs['text']
        question = 'Does the clause specify a minimum order size or minimum amount or units pertime period that one party must buy from the counterparty?'
        answer = row.answer
    elif row.task in ['cuad_most_favored_nation']:
        context = row.inputs['text']
        question = 'Does the clause state that if a third party gets better terms on the licensing or sale of technology/goods/services described in the contract, the buyer of such technology/goods/services under the contract shall be entitled to those better terms?'
        answer = row.answer
    elif row.task in ['cuad_no-solicit_of_customers']:
        context = row.inputs['text']
        question = 'Does the clause restrict a party from contracting or soliciting customers or partners of the counterparty, whether during the contract or after the contract ends (or both)?'
        answer = row.answer
    elif row.task in ['cuad_no-solicit_of_employees']:
        context = row.inputs['text']
        question = 'Does the clause restrict a party’s soliciting or hiring employees and/or contractors from the counterparty, whether during the contract or after the contract ends (or both)?'
        answer = row.answer
    elif row.task in ['cuad_non-compete']:
        context = row.inputs['text']
        question = 'Does the clause restrict the ability of a party to compete with the counterparty or operate in a certain geography or business or technology sector?'
        answer = row.answer
    elif row.task in ['cuad_non-disparagement']:
        context = row.inputs['text']
        question = 'Does the clause require a party not to disparage the counterparty?'
        answer = row.answer
    elif row.task in ['cuad_non-transferable_license']:
        context = row.inputs['text']
        question = 'Does the clause limit the ability of a party to transfer the license being granted to a third party?'
        answer = row.answer
    elif row.task in ['cuad_notice_period_to_terminate_renewal']:
        context = row.inputs['text']
        question = 'Does the clause specify a notice period required to terminate renewal?'
        answer = row.answer
    elif row.task in ['cuad_post-termination_services']:
        context = row.inputs['text']
        question = 'Does the clause subject a party to obligations after the termination or expiration of a contract, including any post-termination transition, payment, transfer of IP, wind-down, last-buy, or similar commitments?'
        answer = row.answer
    elif row.task in ['cuad_price_restrictions']:
        context = row.inputs['text']
        question = 'Does the clause place a restriction on the ability of a party to raise or reduce prices of technology, goods, or services provided?'
        answer = row.answer
    elif row.task in ['cuad_renewal_term']:
        context = row.inputs['text']
        question = 'Does the clause specify a renewal term?'
        answer = row.answer
    elif row.task in ['cuad_revenue-profit_sharing']:
        context = row.inputs['text']
        question = 'Does the clause require a party to share revenue or profit with the counterparty for any technology, goods, or services?'
        answer = row.answer
    elif row.task in ['cuad_rofr-rofo-rofn']:
        context = row.inputs['text']
        question = 'Does the clause grant one party a right of first refusal, right of first offer or right of first negotiation to purchase, license, market, or distribute equity interest, technology, assets, products or services?'
        answer = row.answer
    elif row.task in ['cuad_source_code_escrow']:
        context = row.inputs['text']
        question = 'Does the clause require one party to deposit its source code into escrow with a third party, which can be released to the counterparty upon the occurrence of certain events (bankruptcy, insolvency, etc.)?'
        answer = row.answer
    elif row.task in ['cuad_termination_for_convenience']:
        context = row.inputs['text']
        question = 'Does the clause specify that one party can terminate this contract without cause (solely by giving a notice and allowing a waiting period to expire)?'
        answer = row.answer
    elif row.task in ['cuad_third_party_beneficiary']:
        context = row.inputs['text']
        question = 'Does the clause specify that that there a non-contracting party who is a beneficiary to some or all of the clauses in the contract and therefore can enforce its rights against a contracting party?'
        answer = row.answer
    elif row.task in ['cuad_uncapped_liability']:
        context = row.inputs['text']
        question = 'Does the clause specify that a party’s liability is uncapped upon the breach of its obligation in the contract? This also includes uncap liability for a particular type of breach such as IP infringement or breach of confidentiality obligation'
        answer = row.answer
    elif row.task in ['cuad_unlimited-all-you-can-eat-license']:
        context = row.inputs['text']
        question = 'Does the clause grant one party an “enterprise,” “all you can eat” or unlimited usage license?'
        answer = row.answer
    elif row.task in ['cuad_volume_restriction']:
        context = row.inputs['text']
        question = 'Does the clause specify a fee increase or consent requirement, etc. if one party’s use of the product/services exceeds certain threshold?'
        answer = row.answer
    elif row.task in ['cuad_warranty_duration']:
        context = row.inputs['text']
        question = 'Does the clause specify a  duration of any warranty against defects or errors in technology, products, or services provided under the contract?'
        answer = row.answer
    elif row.task in ['definition_classification']:
        context = row.inputs['text']
        question = 'Identify if the sentence defines a term.'
        answer = row.answer
    elif row.task in ['definition_extraction']:
        context = row.inputs['text']
        question = 'Identify the term being defined in each sentence.'
        answer = row.answer
    elif row.task in ['function_of_decision_section']:
        context = row.inputs['Paragraph']
        question = 'Classify the following text using the following definitions.\n\n- Facts: The paragraph describes the faction background that led up to the present lawsuit.\n- Procedural History: The paragraph describes the course of litigation that led to the current proceeding before the court.\n- Issue: The paragraph describes the legal or factual issue that must be resolved by the court.\n- Rule: The paragraph describes a rule of law relevant to resolving the issue.\n- Analysis: The paragraph analyzes the legal issue by applying the relevant legal principles to the facts of the present dispute.\n- Conclusion: The paragraph presents a conclusion of the court.\n- Decree: The paragraph constitutes a decree resolving the dispute.'
        answer = row.answer
    elif row.task in ['hearsay']:
        context = row.inputs['text']
        question = 'Hearsay is an out-of-court statement introduced to prove the truth of the matter asserted. Is there hearsay?'
        answer = row.answer
    elif row.task in ['insurance_policy_interpretation']:
        context = 'Policy: ' + row.inputs['policy'] + '\n' + 'Claim: ' + row.inputs['claim']
        question = 'Read the insurance policy and the insurance claim. Answer whether the claim is covered under the policy with [A: Yes; B: No; C: It’s ambiguous]'
        answer = row.answer
    elif row.task in ['international_citizenship_questions']:
        context = ''
        question = 'Consider the country of Ethiopia. Does the country provide for involuntary loss of citizenship by a person who renders (non- military) services to a foreign country and, if so, under which conditions?'
        answer = row.answer
    elif row.task in ['jcrew_blocker']:
        context = 'The JCrew Blocker is a provision that typically includes (1) a prohibition on the borrower from transferring IP to an unrestricted subsidiary, and (2) a requirement that the borrower obtains the consent of its agent/lenders before transferring IP to any subsidiary.' + '\n' + 'Provision: ' + row.inputs['text']
        question = 'Does the provision contain JCrew Blockers?'
        answer = row.answer
    elif row.task in ['learned_hands_benefits']:
        context = row.inputs['text']
        question = 'Does the post discuss public benefits and social services that people can get from the government, like for food, disability, old age, housing, medical help, unemployment, child care, or other social needs?'
        answer = row.answer
    elif row.task in ['learned_hands_business']:
        context = row.inputs['text']
        question = 'Does the post discuss issues faced by people who run small businesses or nonprofits, including around incorporation, licenses, taxes, regulations, and other concerns. It also includes options when there are disasters, bankruptcies, or other problems?'
        answer = row.answer
    elif row.task in ['learned_hands_consumer']:
        context = row.inputs['text']
        question = 'Does the post discuss issues people face regarding money, insurance, consumer goods and contracts, taxes, and small claims about quality of service?'
        answer = row.answer
    elif row.task in ['learned_hands_courts']:
        context = row.inputs['text']
        question = 'Does the post discuss the logistics of how a person can interact with a lawyer or the court system. It applies to situations about procedure, rules, how to file lawsuits, how to hire lawyers, how to represent oneself, and other practical matters about dealing with these systems?'
        answer = row.answer
    elif row.task in ['learned_hands_crime']:
        context = row.inputs['text']
        question = 'Does the post discuss issues in the criminal system including when people are charged with crimes, go to a criminal trial, go to prison, or are a victim of a crime?'
        answer = row.answer
    elif row.task in ['learned_hands_divorce']:
        context = row.inputs['text']
        question = 'Does the post discuss issues around filing for divorce, separation, or annulment, getting spousal support, splitting money and property, and following the court processes?'
        answer = row.answer
    elif row.task in ['learned_hands_domestic_violence']:
        context = row.inputs['text']
        question = 'Does the post discuss dealing with domestic violence and abuse, including getting protective orders, enforcing them, understanding abuse, reporting abuse, and getting resources and status if there is abuse?'
        answer = row.answer
    elif row.task in ['learned_hands_education']:
        context = row.inputs['text']
        question = 'Does the post discuss issues around school, including accommodations for special needs, discrimination, student debt, discipline, and other issues in education?'
        answer = row.answer
    elif row.task in ['learned_hands_employment']:
        context = row.inputs['text']
        question = 'Does the post discuss issues related to working at a job, including discrimination and harassment, worker\'s compensation, workers rights, unions, getting paid, pensions, being fired, and more?'
        answer = row.answer
    elif row.task in ['learned_hands_estates']:
        context = row.inputs['text']
        question = 'Does the post discuss planning for end-of-life, possible incapacitation, and other special circumstances that would prevent a person from making decisions about their own well-being, finances, and property. This includes issues around wills, powers of attorney, advance directives, trusts, guardianships, conservatorships, and other estate issues that people and families deal with?'
        answer = row.answer
    elif row.task in ['learned_hands_family']:
        context = row.inputs['text']
        question = 'Does the post discuss issues that arise within a family, like divorce, adoption, name change, guardianship, domestic violence, child custody, and other issues?'
        answer = row.answer
    elif row.task in ['learned_hands_health']:
        context = row.inputs['text']
        question = 'Does the post discuss issues with accessing health services, paying for medical care, getting public benefits for health care, protecting one\'s rights in medical settings, and other issues related to health?'
        answer = row.answer
    elif row.task in ['learned_hands_housing']:
        context = row.inputs['text']
        question = 'Does the post discuss issues with paying your rent or mortgage, landlord-tenant issues, housing subsidies and public housing, eviction, and other problems with your apartment, mobile home, or house?'
        answer = row.answer
    elif row.task in ['learned_hands_immigration']:
        context = row.inputs['text']
        question = 'Does the post discuss visas, asylum, green cards, citizenship, migrant work and benefits, and other issues faced by people who are not full citizens in the US?'
        answer = row.answer
    elif row.task in ['learned_hands_torts']:
        context = row.inputs['text']
        question = 'Does the post discuss problems that one person has with another person (or animal), like when there is a car accident, a dog bite, bullying or possible harassment, or neighbors treating each other badly?'
        answer = row.answer
    elif row.task in ['learned_hands_traffic']:
        context = row.inputs['text']
        question = 'Does the post discuss problems with traffic and parking tickets, fees, driver\'s licenses, and other issues experienced with the traffic system. It also concerns issues with car accidents and injuries, cars\' quality, repairs, purchases, and other contracts?'
        answer = row.answer
    elif row.task in ['legal_reasoning_causality']:
        context = row.inputs['text']
        question = 'Does the following opinion excerpt rely on statistical evidence? Answer Yes or No.'
        answer = row.answer
    elif row.task in ['maud_ability_to_consummate_concept_is_subject_to_mae_carveouts']:
        context = row.inputs['text']
        question = 'Read the segment of a merger agreement and answer the multiple-choice question by choosing the option that best characterizes the agreement.\nIs the “ability to consummate” concept subject to Material Adverse Effect (MAE) carveouts?\nOption A: No\nOption B: Yes'
        answer = row.answer
    elif row.task in ['maud_accuracy_of_fundamental_target_rws_bringdown_standard']:
        context = row.inputs['text']
        question = 'Read the segment of a merger agreement and answer the multiple-choice question by choosing the option that best characterizes the agreement. How accurate must the fundamental representations and warranties be according to the bring down provision?\nOption A: Accurate at another materiality standard (e.g., hybrid standard)\nOption B: Accurate in all material respects\nOption C: Accurate in all respects'
        answer = row.answer
    elif row.task in ['maud_accuracy_of_target_capitalization_rw_(outstanding_shares)_bringdown_standard_answer']:
        context = row.inputs['text']
        question = 'Read the segment of a merger agreement and answer the multiple-choice question by choosing the option that best characterizes the agreement. How accurate must the capitalization representations and warranties be according to the bring down provision?\nOption A: Accurate in all material respects\nOption B: Accurate in all respects\nOption C: Accurate in all respects with below-threshold carveout\nOption D: Accurate in all respects with de minimis exception'
        answer = row.answer
    elif row.task in ['maud_accuracy_of_target_general_rw_bringdown_timing_answer']:
        context = row.inputs['text']
        question = 'Read the segment of a merger agreement and answer the multiple-choice question by choosing the option that best characterizes the agreement. When are representations and warranties required to be made according to the bring down provision?\nOption A: At Closing Only\nOption B: At Signing & At Closing'
        answer = row.answer
    elif row.task in ['maud_additional_matching_rights_period_for_modifications_(cor)']:
        context = row.inputs['text']
        question = 'Read the segment of a merger agreement and answer the multiple-choice question by choosing the option that best characterizes the agreement. How long is the additional matching rights period for modifications in case the board changes its recommendation?\nOption A: 2 business days or less\nOption B: 3 business days\nOption C: 3 days\nOption D: 4 business days\nOption E: 5 business days\nOption F: > 5 business days\nOption G: None'
        answer = row.answer
    elif row.task in ['maud_application_of_buyer_consent_requirement_(negative_interim_covenant)']:
        context = row.inputs['text']
        question = 'Read the segment of a merger agreement and answer the multiple-choice question by choosing the option that best characterizes the agreement. What negative covenants does the requirement of Buyer consent apply to?\nOption A: Applies only to specified negative covenants\nOption B: Applies to all negative covenants'
        answer = row.answer
    elif row.task in ['maud_buyer_consent_requirement_(ordinary_course)']:
        context = row.inputs['text']
        question = 'Read the segment of a merger agreement and answer the multiple-choice question by choosing the option that best characterizes the agreement. In case the Buyer’s consent for the acquired company’s ordinary business operations is required, are there any limitations on the Buyer’s right to condition, withhold, or delay their consent?\nOption A: Yes. Consent may not be unreasonably withheld, conditioned or delayed.\nOption B: No.'
        answer = row.answer
    elif row.task in ['maud_change_in_law__subject_to_disproportionate_impact_modifier']:
        context = row.inputs['text']
        question = 'Read the segment of a merger agreement and answer the multiple-choice question by choosing the option that best characterizes the agreement. Do changes in law that have disproportionate impact qualify for Material Adverse Effect (MAE)?\nOption A: No\nOption B: Yes'
        answer = row.answer
    elif row.task in ['maud_changes_in_gaap_or_other_accounting_principles__subject_to_disproportionate_impact_modifier']:
        context = row.inputs['text']
        question = 'Read the segment of a merger agreement and answer the multiple-choice question by choosing the option that best characterizes the agreement. Do changes in GAAP or other accounting principles that have disproportionate impact qualify for Material Adverse Effect (MAE)?\nOption A: No\nOption B: Yes'
        answer = row.answer
    elif row.task in ['maud_cor_permitted_in_response_to_intervening_event']:
        context = row.inputs['text']
        question = 'Read the segment of a merger agreement and answer the multiple-choice question by choosing the option that best characterizes the agreement. Is Change of Recommendation permitted in response to an intervening event?\nOption A: No\nOption B: Yes'
        answer = row.answer
    elif row.task in ['maud_cor_permitted_with_board_fiduciary_determination_only']:
        context = row.inputs['text']
        question = 'Read the segment of a merger agreement and answer the multiple-choice question by choosing the option that best characterizes the agreement. Is Change of Recommendation permitted as long as the board determines that such change is required to fulfill its fiduciary obligations?\nOption A: No\nOption B: Yes'
        answer = row.answer
    elif row.task in ['maud_cor_standard_(intervening_event)']:
        context = row.inputs['text']
        question = 'Read the segment of a merger agreement and answer the multiple-choice question by choosing the option that best characterizes the agreement. What standard should the board follow when determining whether to change its recommendation in response to an intervening event?\nOption A: "Breach" of fiduciary duties\nOption B: "Inconsistent" with fiduciary duties\nOption C: "Reasonably likely/expected breach" of fiduciary duties\nOption D: "Reasonably likely/expected to be inconsistent" with fiduciary duties\nOption E: "Reasonably likely/expected violation" of fiduciary duties\nOption F: "Required to comply" with fiduciary duties\nOption G: "Violation" of fiduciary duties\nOption H: More likely than not violate fiduciary duties\nOption I: Other specified standard'
        answer = row.answer
    elif row.task in ['maud_cor_standard_(superior_offer)']:
        context = row.inputs['text']
        question = 'Read the segment of a merger agreement and answer the multiple-choice question by choosing the option that best characterizes the agreement. What standard should the board follow when determining whether to change its recommendation in connection with a superior offer?\nOption A: "Breach" of fiduciary duties\nOption B: "Inconsistent" with fiduciary duties\nOption C: "Reasonably likely/expected breach" of fiduciary duties\nOption D: "Reasonably likely/expected to be inconsistent" with fiduciary duties\nOption E: "Reasonably likely/expected violation" of fiduciary duties\nOption F: "Required to comply" with fiduciary duties\nOption G: "Violation" of fiduciary duties\nOption H: More likely than not violate fiduciary duties\nOption I: None\nOption J: Other specified standard'
        answer = row.answer
    elif row.task in ['maud_definition_contains_knowledge_requirement_-_answer']:
        context = row.inputs['text']
        question = 'Read the segment of a merger agreement and answer the multiple-choice question by choosing the option that best characterizes the agreement. What is the knowledge requirement in the definition of “Intervening Event”?\nOption A: Known, but consequences unknown or not reasonably foreseeable, at signing\nOption B: Known, but consequences unknown, at signing\nOption C: Not known and not reasonably foreseeable at signing\nOption D: Not known at signing'
        answer = row.answer
    elif row.task in ['maud_definition_includes_asset_deals']:
        context = row.inputs['text']
        question = 'Read the segment of a merger agreement and answer the multiple-choice question by choosing the option that best characterizes the agreement. What qualifies as a superior offer in terms of asset deals?\nOption A: "All or substantially all"\nOption B: 50%\nOption C: Greater than 50% but not "all or substantially all"\nOption D: Less than 50%'
        answer = row.answer
    elif row.task in ['maud_definition_includes_stock_deals']:
        context = row.inputs['text']
        question = 'Read the segment of a merger agreement and answer the multiple-choice question by choosing the option that best characterizes the agreement. What qualifies as a superior offer in terms of stock deals?\nOption A: "All or substantially all"\nOption B: 50%\nOption C: Greater than 50% but not "all or substantially all"\nOption D: Less than 50%'
        answer = row.answer
    elif row.task in ['maud_fiduciary_exception__board_determination_standard']:
        context = row.inputs['text']
        question = 'Read the segment of a merger agreement and answer the multiple-choice question by choosing the option that best characterizes the agreement. Under what circumstances could the Board take actions on a different acquisition proposal notwithstanding the no-shop provision?\nOption A: If failure to take actions would lead to "breach" of fiduciary duties\nOption B: If failure to take actions would be "inconsistent" with fiduciary duties\nOption C: If failure to take actions would lead to "reasonably likely/expected breach" of fiduciary duties\nOption D: If failure to take actions would lead to "reasonably likely/expected to be inconsistent" with fiduciary duties\nOption E: If failure to take actions would lead to "reasonably likely/expected violation" of fiduciary duties\nOption F: If taking such actions is "required to comply" with fiduciary duties\nOption G: If failure to take actions would lead to "violation" of fiduciary duties\nOption H: Under no circumstances could the Board do so.\nOption I: Other circumstances'
        answer = row.answer
    elif row.task in ['maud_fiduciary_exception_board_determination_trigger_(no_shop)']:
        context = row.inputs['text']
        question = 'Read the segment of a merger agreement and answer the multiple-choice question by choosing the option that best characterizes the agreement. What type of offer could the Board take actions on notwithstanding the no-shop provision?\nOption A: Acquisition Proposal only\nOption B: Superior Offer, or Acquisition Proposal reasonably likely/expected to result in a Superior Offer'
        answer = row.answer
    elif row.task in ['maud_financial_point_of_view_is_the_sole_consideration']:
        context = row.inputs['text']
        question = 'Read the segment of a merger agreement and answer the multiple-choice question by choosing the option that best characterizes the agreement. Is “financial point of view” the sole consideration when determining whether an offer is superior?\nOption A: No\nOption B: Yes'
        answer = row.answer
    elif row.task in ['maud_fls_(mae)_standard']:
        context = row.inputs['text']
        question = 'Read the segment of a merger agreement and answer the multiple-choice question by choosing the option that best characterizes the agreement. What is the Forward Looking Standard (FLS) with respect to Material Adverse Effect (MAE)?\nOption A: "Could" (reasonably) be expected to\nOption B: "Would"\nOption C: "Would" (reasonably) be expected to\nOption D: No\nOption E: Other forward-looking standard'
        answer = row.answer
    elif row.task in ['maud_general_economic_and_financial_conditions_subject_to_disproportionate_impact_modifier']:
        context = row.inputs['text']
        question = 'Read the segment of a merger agreement and answer the multiple-choice question by choosing the option that best characterizes the agreement. Do changes caused by general economic and financial conditions that have disproportionate impact qualify for Material Adverse Effect (MAE)?\nOption A: No\nOption B: Yes'
        answer = row.answer
    elif row.task in ['maud_includes_consistent_with_past_practice']:
        context = row.inputs['text']
        question = 'Read the segment of a merger agreement and answer the multiple-choice question by choosing the option that best characterizes the agreement. Does the wording of the Efforts Covenant clause include “consistent with past practice”?\nOption A: No\nOption B: Yes'
        answer = row.answer
    elif row.task in ['maud_initial_matching_rights_period_(cor)']:
        context = row.inputs['text']
        question = 'Read the segment of a merger agreement and answer the multiple-choice question by choosing the option that best characterizes the agreement. How long is the initial matching rights period in case the board changes its recommendation?\nOption A: 2 business days or less\nOption B: 3 business days\nOption C: 3 calendar days\nOption D: 4 business days\nOption E: 4 calendar days\nOption F: 5 business days\nOption G: Greater than 5 business days'
        answer = row.answer
    elif row.task in ['maud_initial_matching_rights_period_(ftr)']:
        context = row.inputs['text']
        question = 'Read the segment of a merger agreement and answer the multiple-choice question by choosing the option that best characterizes the agreement. How long is the initial matching rights period in connection with the Fiduciary Termination Right (FTR)?\nOption A: 2 business days or less\nOption B: 3 business days\nOption C: 3 calendar days\nOption D: 4 business days\nOption E: 4 calendar days\nOption F: 5 business days\nOption G: 5 calendar days\nOption H: Greater than 5 business days'
        answer = row.answer
    elif row.task in ['maud_intervening_event_-_required_to_occur_after_signing_-_answer']:
        context = row.inputs['text']
        question = 'Read the segment of a merger agreement and answer the multiple-choice question by choosing the option that best characterizes the agreement. Is an "Intervening Event" required to occur after signing?\nOption A: No. It may occur or arise prior to signing.\nOption B: Yes. It must occur or arise after signing.'
        answer = row.answer
    elif row.task in ['maud_knowledge_definition']:
        context = row.inputs['text']
        question = 'Read the segment of a merger agreement and answer the multiple-choice question by choosing the option that best characterizes the agreement. What counts as Knowledge?\nOption A: Actual knowledge\nOption B: Constructive knowledge'
        answer = row.answer
    elif row.task in ['maud_liability_standard_for_no-shop_breach_by_target_non-do_representatives']:
        context = row.inputs['text']
        question = 'Read the segment of a merger agreement and answer the multiple-choice question by choosing the option that best characterizes the agreement. What is the liability standard for no-shop breach by Target Non-D&O Representatives?\nOption A: Reasonable standard\nOption B: Strict liability'
        answer = row.answer
    elif row.task in ['maud_ordinary_course_efforts_standard']:
        context = row.inputs['text']
        question = 'Read the segment of a merger agreement and answer the multiple-choice question by choosing the option that best characterizes the agreement. What is the efforts standard?\nOption A: Commercially reasonable efforts\nOption B: Flat covenant (no efforts standard)\nOption C: Reasonable best efforts'
        answer = row.answer
    elif row.task in ['maud_pandemic_or_other_public_health_event__subject_to_disproportionate_impact_modifier']:
        context = row.inputs['text']
        question = 'Read the segment of a merger agreement and answer the multiple-choice question by choosing the option that best characterizes the agreement. Do pandemics or other public health events have to have disproportionate impact to qualify for Material Adverse Effect (MAE)?\nOption A: No\nOption B: Yes'
        answer = row.answer
    elif row.task in ['maud_pandemic_or_other_public_health_event_specific_reference_to_pandemic-related_governmental_responses_or_measures']:
        context = row.inputs['text']
        question = 'Read the segment of a merger agreement and answer the multiple-choice question by choosing the option that best characterizes the agreement. Is there specific reference to pandemic-related governmental responses or measures in the clause that qualifies pandemics or other public health events for Material Adverse Effect (MAE)?\nOption A: No\nOption B: Yes'
        answer = row.answer
    elif row.task in ['maud_relational_language_(mae)_applies_to']:
        context = row.inputs['text']
        question = 'Read the segment of a merger agreement and answer the multiple-choice question by choosing the option that best characterizes the agreement. What carveouts pertaining to Material Adverse Effect (MAE) does the relational language apply to?\nOption A: All MAE carveouts\nOption B: No\nOption C: Some MAE carveouts'
        answer = row.answer
    elif row.task in ['maud_specific_performance']:
        context = row.inputs['text']
        question = 'Read the segment of a merger agreement and answer the multiple-choice question by choosing the option that best characterizes the agreement. What is the wording of the Specific Performance clause regarding the parties’ entitlement in the event of a contractual breach?\nOption A: "entitled to seek" specific performance\nOption B: "entitled to" specific performance'
        answer = row.answer
    elif row.task in ['maud_tail_period_length']:
        context = row.inputs['text']
        question = 'Read the segment of a merger agreement and answer the multiple-choice question by choosing the option that best characterizes the agreement. How long is the Tail Period?\nOption A: 12 months or longer\nOption B: Other\nOption C: within 12 months\nOption D: within 6 months\nOption E: within 9 months'
        answer = row.answer
    elif row.task in ['maud_type_of_consideration']:
        context = row.inputs['text']
        question = 'Read the segment of a merger agreement and answer the multiple-choice question by choosing the option that best characterizes the agreement. What type of consideration is specified in this agreement?\nOption A: All Cash\nOption B: All Stock\nOption C: Mixed Cash/Stock\nOption D: Mixed Cash/Stock: Election'
        answer = row.answer
    elif row.task in ['nys_judicial_ethics']:
        context = ''
        question = 'Imagine your are the New York State Unified Court System Advisory Committee on Judicial Ethics. You\'ve received the following question. Answer it as either "Yes" or "No".\n' + row.inputs['question']
        answer = row.answer
    elif row.task in ['opp115_data_retention']:
        context = row.inputs['text']
        question = 'Does the clause describe how long user information is stored?'
        answer = row.answer
    elif row.task in ['opp115_data_security']:
        context = row.inputs['text']
        question = 'Does the clause describe how user information is protected?'
        answer = row.answer
    elif row.task in ['opp115_do_not_track']:
        context = row.inputs['text']
        question = 'Does the clause describe if and how Do Not Track signals for online tracking and advertising are honored?'
        answer = row.answer
    elif row.task in ['opp115_first_party_collection_use']:
        context = row.inputs['text']
        question = 'Does the clause describe how and why a service provider collects user information?'
        answer = row.answer
    elif row.task in ['opp115_international_and_specific_audiences']:
        context = row.inputs['text']
        question = 'Does the clause describe practices that pertain only to a specific group of users (e.g., children, Europeans, or California residents)?'
        answer = row.answer
    elif row.task in ['opp115_policy_change']:
        context = row.inputs['text']
        question = 'Does the clause describe if and how users will be informed about changes to the privacy policy?'
        answer = row.answer
    elif row.task in ['opp115_third_party_sharing_collection']:
        context = row.inputs['text']
        question = 'Does the clause describe how user information may be shared with or collected by third parties?'
        answer = row.answer
    elif row.task in ['opp115_user_access,_edit_and_deletion']:
        context = row.inputs['text']
        question = 'Does the clause describe if and how users may access, edit, or delete their information?'
        answer = row.answer
    elif row.task in ['opp115_user_choice_control']:
        context = row.inputs['text']
        question = 'Does the clause describe the choices and control options available to users?'
        answer = row.answer
    elif row.task in ['oral_argument_question_purpose']:
        context = row.inputs['question']
        question = 'Classify the function that the question serves. Options: Background, Clarification, Communicate, Criticism, Humor, Implications, Support'
        answer = row.answer
    elif row.task in ['overruling']:
        context = row.inputs['text']
        question = 'Does the sentence contain language overruling a previous case?'
        answer = row.answer
    elif row.task in ['personal_jurisdiction']:
        context = 'There is personal jurisdiction over a defendant in the state where the defendant is domiciled, or when (1) the defendant has sufficient contacts with the state, such that they have availed itself of the privileges of the state and (2) the claim arises out of the nexus of the defendant\'s contacts with the state.' + '\n' + row.inputs['text']
        question = 'Is there personal jurisdiction?'
        answer = row.answer
    elif row.task in ['privacy_policy_entailment']:
        context = 'Clause: ' + row.inputs['text'] + '\n' + 'Description: ' + row.inputs['description']
        question = 'Classify if the description of the clause is correct.'
        answer = row.answer
    elif row.task in ['privacy_policy_qa']:
        context = 'Clause: ' + row.inputs['text'] + '\n' + 'Question: ' + row.inputs['question']
        question = 'Classify if the clause is relevant to answering the question.'
        answer = row.answer
    elif row.task in ['proa']:
        context = row.inputs['text']
        question = 'A private right of action is when a regular person, a private citizen, is legally entitled to enforce their rights under a given statute. Does the clause specify a private right of action?'
        answer = row.answer
    elif row.task in ['sara_entailment']:
        context = "Statue: " + row.inputs['statute'] + "\nDescription: " + row.inputs['description'] + "\nStatement: " + row.inputs['question']
        question = 'Determine whether the following statements are entailed under the statute.'
        answer = row.answer
    elif row.task in ['sara_numeric']:
        context = 'Statue: ' + row.inputs['statute'] + '\nDescription: ' + row.inputs['description']
        question = 'Answer the following question.\n' + row.inputs['question']
        answer = row.answer
    elif row.task in ['scalr']:
        context = ''
        question = 'Given the following question presented in a court case, select the most relevant holding.\n' + row.inputs['question'] + '\nChoices:' + '\n0: ' + row.inputs['choice_0'] + '\n1: ' + row.inputs['choice_1'] + '\n2: ' + row.inputs['choice_2'] + '\n3: ' + row.inputs['choice_3'] + '\n4: ' + row.inputs['choice_4']
        answer = row.answer
    elif row.task in ['ssla_company_defendants']:
        context = row.inputs['text']
        question = 'From the excerpt, extract the names of the defendants that are companies.'
        answer = row.answer
    elif row.task in ['ssla_individual_defendants']:
        context = row.inputs['text']
        question = 'From the excerpt, extract the names of the defendants that are individuals.'
        answer = row.answer
    elif row.task in ['ssla_plaintiff']:
        context = row.inputs['text']
        question = 'Extract the name(s) of the plaintiff from the excerpt. If the plaintiff is not named, return "Not named"'
        answer = row.answer.replace('[\'', '').replace('\']', '')
    elif row.task in ['successor_liability']:
        context = 'When one company sells its assets to another company, the purchaser is generally not liable for the seller\'s debts and liabilities. There are four exceptions:\n1. the purchaser expressly agrees to be held liable (express agreement)\n2. the assets are fraudulently conveyed to the purchaser in order to avoid liability (fraudulent conveyance)\n3. there is a de facto merger between the purchaser and seller (de facto merger)\n4. the purchaser is a mere continuation of the seller (mere continuation)' + '\n' + row.inputs['text']
        question = 'For the following fact pattern, determine which exceptions apply.'
        answer = row.answer
    elif row.task in ['supply_chain_disclosure_best_practice_accountability']:
        context = row.inputs['text']
        question = 'Does the above disclosure meet the following criteria: Does the above statement disclose whether the retail seller or manufacturer maintains internal compliance procedures on company standards regarding human trafficking and slavery? This includes any type of internal accountability mechanism. Requiring independently of the supply to comply with laws does not qualify or asking for documentary evidence of compliance does not count either.  Answer yes or no.'
        answer = row.answer
    elif row.task in ['supply_chain_disclosure_best_practice_audits']:
        context = row.inputs['text']
        question = 'Does the above disclosure meet the following criteria: Does the above statement disclose whether the retail seller or manufacturer  performs any type of audit, or reserves the right to audit? Answer yes or no.'
        answer = row.answer
    elif row.task in ['supply_chain_disclosure_best_practice_certification']:
        context = row.inputs['text']
        question = 'Question: Does the above disclosure meet the following criteria: Does the above statement disclose whether the retail seller or manufacturer requires direct suppliers to certify that they comply with labor and anti-trafficking laws? Answer yes or no.'
        answer = row.answer
    elif row.task in ['supply_chain_disclosure_best_practice_training']:
        context = row.inputs['text']
        question = 'Does the above disclosure meet the following criteria: Does the above statement disclose whether the retail seller or manufacturer  provides training to employees on human trafficking and slavery? Broad policies such as ongoing dialogue on mitigating risks of human trafficking and slavery or increasing managers and purchasers knowledge about health, safety and labor practices qualify as training. Providing training to contractors who failed to comply with human trafficking laws counts as training.  Answer yes or no.'
        answer = row.answer
    elif row.task in ['supply_chain_disclosure_best_practice_verification']:
        context = row.inputs['text']
        question = 'Does the above disclosure meet the following criteria: Does the above statement disclose whether the retail seller or manufacturer engages in verification and auditing as one practice, expresses that it may conduct an audit, or expressess that it is assessing supplier risks through a review of the US Dept. of Labor\'s List? Answer yes or no.'
        answer = row.answer
    elif row.task in ['supply_chain_disclosure_disclosed_accountability']:
        context = row.inputs['text']
        question = 'Does the above disclosure meet the following criteria: Does the above statement disclose to what extent, if any, that the retail seller or manufacturer maintains internal accountability standards and procedures for employees or contractors failing to meet company standards regarding slavery and trafficking? Answer yes or no.'
        answer = row.answer
    elif row.task in ['supply_chain_disclosure_disclosed_audits']:
        context = row.inputs['text']
        question = 'Does the above disclosure meet the following criteria: Does the above statement disclose to what extent, if any, that the retail seller or manufacturer conducts audits of suppliers to evaluate supplier compliance with company standards for trafficking and slavery in supply chains? The disclosure shall specify if the verification was not an independent, unannounced audit. Answer yes or no.'
        answer = row.answer
    elif row.task in ['supply_chain_disclosure_disclosed_certification']:
        context = row.inputs['text']
        question = 'Does the above disclosure meet the following criteria: Does the above statement disclose to what extent, if any, that the retail seller or manufacturer requires direct suppliers to certify that materials incorporated into the product comply with the laws regarding slavery and human trafficking of the country or countries in which they are doing business? Answer yes or no.'
        answer = row.answer
    elif row.task in ['supply_chain_disclosure_disclosed_training']:
        context = row.inputs['text']
        question = 'Does the above disclosure meet the following criteria: Does the above statement disclose to what extent, if any, that the retail seller or manufacturer provides company employees and management, who have direct responsibility for supply chain management, training on human trafficking and slavery, particularly with respect to mitigating risks within the supply chains of products? Answer yes or no.'
        answer = row.answer
    elif row.task in ['supply_chain_disclosure_disclosed_verification']:
        context = row.inputs['text']
        question = 'Does the above disclosure meet the following criteria: Does the above statement disclose to what extent, if any, that the retail seller or manufacturer engages in verification of product supply chains to evaluate and address risks of human trafficking and slavery? If the company conducts verification], the disclosure shall specify if the verification was not conducted by a third party. Answer yes or no.'
        answer = row.answer
    elif row.task in ['telemarketing_sales_rule']:
        context = 'The Telemarketing Sales Rule is provided by 16 C.F.R. § 310.3(a)(1) and 16 C.F.R. § 310.3(a)(2).'
        question = row.inputs['text']
        answer = row.answer
    elif row.task in ['textualism_tool_dictionaries']:
        context = row.inputs['text']
        question = 'Label "Yes" if the paragraph interprets a statue using a dictionary definition for terms in the statute. The paragraph must reference that it is using a dictionary, or discuss the logic behind using a dictionary. Otherwise label "No".'
        answer = row.answer
    elif row.task in ['textualism_tool_plain']:
        context = row.inputs['text']
        question = 'Label "Yes" if the paragraph interprets a statue using the plain or ordinary meaning of the terms in the statute. The paragraph must reference that it is using plain meaning, or discuss the logic behind using plain meaning. Otherwise label "No".'
        answer = row.answer
    elif row.task in ['ucc_v_common_law']:
        context = 'The UCC (through Article 2) governs the sale of goods, which are defined as moveable tangible things (cars, apples, books, etc.), whereas the common law governs contracts for real estate and services. For the following contracts, determine if they are governed by the UCC or by common law.'
        question = row.inputs['contract']
        answer = row.answer
    elif row.task in ['unfair_tos']:
        context = row.inputs['text']
        question = 'Classify each clause by type. Options: Arbitration, Unilateral change, Content removal, Jurisdiction, Choice of law, Limitation of liability, Unilateral termination, Contract by using, Other'
        answer = row.answer
    elif row.task in ['diversity_1', 'diversity_2', 'diversity_3', 'diversity_4', 'diversity_5', 'diversity_6']:
        context = 'Diversity jurisdiction exists when there is (1) complete diversity between plaintiffs and defendants, and (2) the amount-in-controversy (AiC) is greater than $75k.\n' + row.inputs['text']
        question = 'Is there diversity jurisdiction?'
        answer = row.answer
    else:
        raise Exception("Incorrect task.")
    
    return row.index, context, question, answer