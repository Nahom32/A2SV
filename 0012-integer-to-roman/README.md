<h2><a href="https://leetcode.com/problems/integer-to-roman/">12. Integer to Roman</a></h2><h3>Medium</h3><hr><div><p>Roman numerals are represented by seven different symbols:&nbsp;<code>I</code>, <code>V</code>, <code>X</code>, <code>L</code>, <code>C</code>, <code>D</code> and <code>M</code>.</p>

<div class="top-box hide"><div class="alert-info"></div></div><pre data-original-code="Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000" data-snippet-id="ext.3ec7ecda49f6eec1487e489153094b31" data-snippet-saved="false" data-codota-status="done"><strong>Symbol</strong>       <strong>Value</strong>
I             1
V             5
X             10
L             50
C             100
D             500
M             1000</pre>

<p>For example,&nbsp;<code>2</code> is written as <code>II</code>&nbsp;in Roman numeral, just two one's added together. <code>12</code> is written as&nbsp;<code>XII</code>, which is simply <code>X + II</code>. The number <code>27</code> is written as <code>XXVII</code>, which is <code>XX + V + II</code>.</p>

<p>Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not <code>IIII</code>. Instead, the number four is written as <code>IV</code>. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as <code>IX</code>. There are six instances where subtraction is used:</p>

<ul>
	<li><code>I</code> can be placed before <code>V</code> (5) and <code>X</code> (10) to make 4 and 9.&nbsp;</li>
	<li><code>X</code> can be placed before <code>L</code> (50) and <code>C</code> (100) to make 40 and 90.&nbsp;</li>
	<li><code>C</code> can be placed before <code>D</code> (500) and <code>M</code> (1000) to make 400 and 900.</li>
</ul>

<p>Given an integer, convert it to a roman numeral.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="top-box hide"><div class="alert-info"></div></div><pre data-original-code="Input: num = 3
Output: &quot;III&quot;
Explanation: 3 is represented as 3 ones.
" data-snippet-id="ext.cb62398b2cc6d3f9586519562fcced13" data-snippet-saved="false" data-codota-status="done"><strong>Input:</strong> num = 3
<strong>Output:</strong> "III"
<strong>Explanation:</strong> 3 is represented as 3 ones.
</pre>

<p><strong class="example">Example 2:</strong></p>

<div class="top-box hide"><div class="alert-info"></div></div><pre data-original-code="Input: num = 58
Output: &quot;LVIII&quot;
Explanation: L = 50, V = 5, III = 3.
" data-snippet-id="ext.01110b6c31fe71ce372f5c2c0ffd3ca1" data-snippet-saved="false" data-codota-status="done"><strong>Input:</strong> num = 58
<strong>Output:</strong> "LVIII"
<strong>Explanation:</strong> L = 50, V = 5, III = 3.
</pre>

<p><strong class="example">Example 3:</strong></p>

<div class="top-box hide"><div class="alert-info"></div></div><pre data-original-code="Input: num = 1994
Output: &quot;MCMXCIV&quot;
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
" data-snippet-id="ext.838ef265a48083b62a81bf0d812b3003" data-snippet-saved="false" data-codota-status="done"><strong>Input:</strong> num = 1994
<strong>Output:</strong> "MCMXCIV"
<strong>Explanation:</strong> M = 1000, CM = 900, XC = 90 and IV = 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num &lt;= 3999</code></li>
</ul>
</div>