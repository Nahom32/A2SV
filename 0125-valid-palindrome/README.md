<h2><a href="https://leetcode.com/problems/valid-palindrome/">125. Valid Palindrome</a></h2><h3>Easy</h3><hr><div><p>A phrase is a <strong>palindrome</strong> if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.</p>

<p>Given a string <code>s</code>, return <code>true</code><em> if it is a <strong>palindrome</strong>, or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="top-box hide"><div class="alert-info"></div></div><pre data-original-code="Input: s = &quot;A man, a plan, a canal: Panama&quot;
Output: true
Explanation: &quot;amanaplanacanalpanama&quot; is a palindrome.
" data-snippet-id="ext.be9a79f71836db216c1df90552c93ad0" data-snippet-saved="false" data-codota-status="done"><strong>Input:</strong> s = "A man, a plan, a canal: Panama"
<strong>Output:</strong> true
<strong>Explanation:</strong> "amanaplanacanalpanama" is a palindrome.
</pre>

<p><strong class="example">Example 2:</strong></p>

<div class="top-box hide"><div class="alert-info"></div></div><pre data-original-code="Input: s = &quot;race a car&quot;
Output: false
Explanation: &quot;raceacar&quot; is not a palindrome.
" data-snippet-id="ext.9e906e856aceeed8c2f1735b678f2e12" data-snippet-saved="false" data-codota-status="done"><strong>Input:</strong> s = "race a car"
<strong>Output:</strong> false
<strong>Explanation:</strong> "raceacar" is not a palindrome.
</pre>

<p><strong class="example">Example 3:</strong></p>

<div class="top-box hide"><div class="alert-info"></div></div><pre data-original-code="Input: s = &quot; &quot;
Output: true
Explanation: s is an empty string &quot;&quot; after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
" data-snippet-id="ext.74bb19f5aaaa9f446ebe2f78d8742a82" data-snippet-saved="false" data-codota-status="done"><strong>Input:</strong> s = " "
<strong>Output:</strong> true
<strong>Explanation:</strong> s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>s</code> consists only of printable ASCII characters.</li>
</ul>
</div>