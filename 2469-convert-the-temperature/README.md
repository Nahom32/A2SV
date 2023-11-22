<h2><a href="https://leetcode.com/problems/convert-the-temperature/">2469. Convert the Temperature</a></h2><h3>Easy</h3><hr><div><p>You are given a non-negative floating point number rounded to two decimal places <code>celsius</code>, that denotes the <strong>temperature in Celsius</strong>.</p>

<p>You should convert Celsius into <strong>Kelvin</strong> and <strong>Fahrenheit</strong> and return it as an array <code>ans = [kelvin, fahrenheit]</code>.</p>

<p>Return <em>the array <code>ans</code>. </em>Answers within <code>10<sup>-5</sup></code> of the actual answer will be accepted.</p>

<p><strong>Note that:</strong></p>

<ul>
	<li><code>Kelvin = Celsius + 273.15</code></li>
	<li><code>Fahrenheit = Celsius * 1.80 + 32.00</code></li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="top-box hide"><div class="alert-info"></div></div><pre data-original-code="Input: celsius = 36.50
Output: [309.65000,97.70000]
Explanation: Temperature at 36.50 Celsius converted in Kelvin is 309.65 and converted in Fahrenheit is 97.70.
" data-snippet-id="ext.60bebf3064656d549c2fcfb53d880181" data-snippet-saved="false" data-codota-status="done"><strong>Input:</strong> celsius = 36.50
<strong>Output:</strong> [309.65000,97.70000]
<strong>Explanation:</strong> Temperature at 36.50 Celsius converted in Kelvin is 309.65 and converted in Fahrenheit is 97.70.
</pre>

<p><strong class="example">Example 2:</strong></p>

<div class="top-box hide"><div class="alert-info"></div></div><pre data-original-code="Input: celsius = 122.11
Output: [395.26000,251.79800]
Explanation: Temperature at 122.11 Celsius converted in Kelvin is 395.26 and converted in Fahrenheit is 251.798.
" data-snippet-id="ext.4413c6501b4ddce328ccb56bb94b9be4" data-snippet-saved="false" data-codota-status="done"><strong>Input:</strong> celsius = 122.11
<strong>Output:</strong> [395.26000,251.79800]
<strong>Explanation:</strong> Temperature at 122.11 Celsius converted in Kelvin is 395.26 and converted in Fahrenheit is 251.798.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= celsius &lt;= 1000</code></li>
</ul>
</div>