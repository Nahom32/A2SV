<h2><a href="https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/">1456. Maximum Number of Vowels in a Substring of Given Length</a></h2><h3>Medium</h3><hr><div><p>Given a string <code>s</code> and an integer <code>k</code>, return <em>the maximum number of vowel letters in any substring of </em><code>s</code><em> with length </em><code>k</code>.</p>

<p><strong>Vowel letters</strong> in English are <code>'a'</code>, <code>'e'</code>, <code>'i'</code>, <code>'o'</code>, and <code>'u'</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="top-box hide"><div class="alert-info"></div></div><pre data-original-code="Input: s = &quot;abciiidef&quot;, k = 3
Output: 3
Explanation: The substring &quot;iii&quot; contains 3 vowel letters.
" data-snippet-id="ext.d57bd1c3f770cc99a035d0de75f69641" data-snippet-saved="false" data-codota-status="done"><strong>Input:</strong> s = "abciiidef", k = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> The substring "iii" contains 3 vowel letters.
</pre>

<p><strong class="example">Example 2:</strong></p>

<div class="top-box hide"><div class="alert-info"></div></div><pre data-original-code="Input: s = &quot;aeiou&quot;, k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
" data-snippet-id="ext.bb424bec45f5bdaab08e7c1beb36ccf6" data-snippet-saved="false" data-codota-status="done"><strong>Input:</strong> s = "aeiou", k = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> Any substring of length 2 contains 2 vowels.
</pre>

<p><strong class="example">Example 3:</strong></p>

<div class="top-box hide"><div class="alert-info"></div></div><pre data-original-code="Input: s = &quot;leetcode&quot;, k = 3
Output: 2
Explanation: &quot;lee&quot;, &quot;eet&quot; and &quot;ode&quot; contain 2 vowels.
" data-snippet-id="ext.a449a199deaf83e236fe218953cb5d75" data-snippet-saved="false" data-codota-status="done"><strong>Input:</strong> s = "leetcode", k = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> "lee", "eet" and "ode" contain 2 vowels.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
	<li><code>1 &lt;= k &lt;= s.length</code></li>
</ul>
</div>