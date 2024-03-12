
<h2>About the connector</h2>

<p>Cymulate Continuous Automated Red Teaming (CART) validates security controls and responses against real-world cyber attacks to stress-test defenses and identify gaps and does network pen testing, phishing awareness, real world cyber attacks. Users can use this connector to perform automated operations for managing Full Kill-Chain Campaign module data in your Cymulate account</p>

<p>This document provides information about the Cymulate Full Kill Chain Campaign - CART Connector, which facilitates automated interactions, with a Cymulate Full Kill Chain Campaign - CART server using FortiSOAR&trade; playbooks. Add the Cymulate Full Kill Chain Campaign - CART Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Cymulate Full Kill Chain Campaign - CART.</p>

<h3>Version information</h3>

<p>Connector Version: 1.0.0</p>

<p>Authored By: Fortinet</p>

<p>Certified: No</p>

<h2>Installing the connector</h2>

<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>

<pre>yum install cyops-connector-cymulate-full-kill-chain-campaign</pre>

<h2>Prerequisites to configuring the connector</h2>

<ul>
<li>You must have the credentials of Cymulate Full Kill Chain Campaign - CART server to which you will connect and perform automated operations.</li>
<li>The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Cymulate Full Kill Chain Campaign - CART server.</li>
</ul>

<h2>Minimum Permissions Required</h2>

<ul>
<li>Not applicable</li>
</ul>

<h2>Configuring the connector</h2>

<p>For the procedure to configure a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector">here</a></p>

<h3>Configuration parameters</h3>

<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Cymulate Full Kill Chain Campaign - CART</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Specify the Cymulate API server URL to connect and perform the automated operations.</td>
</tr><tr><td>API Key</td><td>Specify the Secret Key of the API Application already created in the Cymulate Server.</td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>

<h2>Actions supported by the connector</h2>

<p>The following automated operations can be included in playbooks and you can also use the annotations to access operations:</p>

<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get Campaign Report</td><td>Retrieve the latest Full Kill-Chain Campaign report results (overview) by the environment ID</td><td>get_campaign_report <br/>Investigation</td></tr>
<tr><td>Get Campaign Assessments IDs</td><td>Retrieve a list of IDs for the latest Full Kill-Chain Campaign assessments.</td><td>get_campaign_assessments_ids <br/>Investigation</td></tr>
<tr><td>Get Technical Report for Specific Assessment</td><td>Retrieve Full Kill-Chain Campaign technical report results for a specific assessment</td><td>get_technical_report_for_specific_assessment <br/>Investigation</td></tr>
<tr><td>Launch Campaign Assessment</td><td>Launch a Full Kill-Chain Campaign assessment with the specified input parameter values</td><td>launch_campaign_assessment <br/>Investigation</td></tr>
<tr><td>Stop Campaign Assessment</td><td>Stop a Full Kill-Chain Campaign assessment that is currently running</td><td>stop_campaign_assessment <br/>Investigation</td></tr>
<tr><td>Get Campaign Assessment History</td><td>Retrieve the Full Kill-Chain Campaign assessment history within the date range</td><td>get_campaign_assessment_history <br/>Investigation</td></tr>
<tr><td>Get Specific Campaign Assessment Report</td><td>Retrieve Full Kill-Chain Campaign report results for a specific assessment</td><td>get_specific_campaign_assessment_report <br/>Investigation</td></tr>
<tr><td>Get Campaign Assessment Status</td><td>Retrieve a Full Kill-Chain Campaign assessment status by the assessment ID</td><td>get_campaign_assessment_status <br/>Investigation</td></tr>
<tr><td>Get Campaign Templates</td><td>Retrieve a list of available Full Kill-Chain Campaign templates</td><td>get_campaign_templates <br/>Investigation</td></tr>
</tbody></table>

<h3>operation: Get Campaign Report</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Environment ID</td><td>Specify the environment ID. If an ID is not provided, the request will return latest report results for the Default environment.
</td></tr></tbody></table>

<h4>Output</h4>

<p>The output contains a non-dictionary value.</p>

<h3>operation: Get Campaign Assessments IDs</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Environment ID</td><td>Specify the environment ID. If an ID is not provided, the request will return return latest data for the Default environment
</td></tr></tbody></table>

<h4>Output</h4>

<p>The output contains a non-dictionary value.</p>

<h3>operation: Get Technical Report for Specific Assessment</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Assessment ID</td><td>Provide an ID for the assessment you want to receive a technical report
</td></tr></tbody></table>

<h4>Output</h4>

<p>The output contains a non-dictionary value.</p>

<h3>operation: Launch Campaign Assessment</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Template ID</td><td>Provide the Template ID for the assessment you wish to launch
</td></tr><tr><td>Schedule Time</td><td>Specify the time to launch the Campaign Assessment
</td></tr><tr><td>Schedule Loop</td><td>Select the loop size of the schedule
</td></tr></tbody></table>

<h4>Output</h4>

<p>The output contains a non-dictionary value.</p>

<h3>operation: Stop Campaign Assessment</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Environment ID</td><td>The environment ID. If an ID is not provided, the most recently launched assessment will be stopped
</td></tr></tbody></table>

<h4>Output</h4>

<p>The output contains a non-dictionary value.</p>

<h3>operation: Get Campaign Assessment History</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Environment ID</td><td>The environment ID. If an ID is not provided, the most recently launched assessment will be stopped
</td></tr><tr><td>From Date</td><td>Specify the date for Full Kill-Chain Campaign assessments from this date
</td></tr><tr><td>To Date</td><td>Specify the date for Full Kill-Chain Campaign assessments until this date
</td></tr></tbody></table>

<h4>Output</h4>

<p>The output contains a non-dictionary value.</p>

<h3>operation: Get Specific Campaign Assessment Report</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Assessment ID</td><td>Specify the ID of the assessment for which you want to obtain a specific assessment report
</td></tr><tr><td>Index</td><td>Specify the index of the first item in the returned list.
</td></tr><tr><td>Limit</td><td>Specify the limit for the number of items to return in the result
</td></tr></tbody></table>

<h4>Output</h4>

<p>The output contains a non-dictionary value.</p>

<h3>operation: Get Campaign Assessment Status</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Assessment ID</td><td>Specify the assessment ID. If an ID is not provided, the request will return the latest run assessment
</td></tr></tbody></table>

<h4>Output</h4>

<p>The output contains a non-dictionary value.</p>

<h3>operation: Get Campaign Templates</h3>

<h4>Input parameters</h4>

<p>None.</p>

<h4>Output</h4>

<p>The output contains a non-dictionary value.</p>

<h2>Included playbooks</h2>

<p>The <code>Sample - cymulate-full-kill-chain-campaign - 1.0.0</code> playbook collection comes bundled with the Cymulate Full Kill Chain Campaign - CART connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the <strong>Automation</strong> &gt; <strong>Playbooks</strong> section in FortiSOAR&trade; after importing the Cymulate Full Kill Chain Campaign - CART connector.</p>

<ul>
<li>Get Campaign Assessment History</li>
<li>Get Campaign Assessment Status</li>
<li>Get Campaign Assessments IDs</li>
<li>Get Campaign Report</li>
<li>Get Campaign Templates</li>
<li>Get Specific Campaign Assessment Report</li>
<li>Get Technical Report for Specific Assessment</li>
<li>Launch Campaign Assessment</li>
<li>Stop Campaign Assessment</li>
</ul>

<p><strong>Note</strong>: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.</p>
