<h2><a href="https://leetcode.com/problems/palindrome-number/">9. Palindrome Number</a></h2><h3>Easy</h3><hr><div><p>Given an integer <code>x</code>, return <code>true</code><em> if </em><code>x</code><em> is a </em><span data-keyword="palindrome-integer"><em><strong>palindrome</strong></em></span><em>, and </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="top-box hide"><div class="alert-info"></div></div><div class="top-box hide"><div class="alert-info"></div></div><pre data-original-code="Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
" data-snippet-id="ext.d7339e43072acecee2b493533563c842" data-snippet-saved="false" data-codota-status="done"><strong>Input:</strong> x = 121
<strong>Output:</strong> true
<strong>Explanation:</strong> 121 reads as 121 from left to right and from right to left.
</pre>

<p><strong class="example">Example 2:</strong></p>

<div class="top-box hide"><div class="alert-info"></div></div><div class="top-box hide"><div class="alert-info"></div></div><pre data-original-code="Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
" data-snippet-id="ext.85bfc467fcd1d5c9d49de9347c0fb4d3" data-snippet-saved="false" data-codota-status="done"><strong>Input:</strong> x = -121
<strong>Output:</strong> false
<strong>Explanation:</strong> From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
</pre>

<p><strong class="example">Example 3:</strong></p>

<div class="top-box hide"><div class="alert-info"></div></div><div class="top-box hide"><div class="alert-info"></div></div><pre data-original-code="Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
" data-snippet-id="ext.232a00e13f0317c9a58fcc23bd94b982" data-snippet-saved="false" data-codota-status="done"><strong>Input:</strong> x = 10
<strong>Output:</strong> false
<strong>Explanation:</strong> Reads 01 from right to left. Therefore it is not a palindrome.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup>&nbsp;&lt;= x &lt;= 2<sup>31</sup>&nbsp;- 1</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you solve it without converting the integer to a string?</div>