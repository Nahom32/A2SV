<h2><a href="https://leetcode.com/problems/find-first-palindromic-string-in-the-array/">2108. Find First Palindromic String in the Array</a></h2><h3>Easy</h3><hr><div><p>Given an array of strings <code>words</code>, return <em>the first <strong>palindromic</strong> string in the array</em>. If there is no such string, return <em>an <strong>empty string</strong> </em><code>""</code>.</p>

<p>A string is <strong>palindromic</strong> if it reads the same forward and backward.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="top-box hide"><div class="alert-info"></div></div><pre data-original-code="Input: words = [&quot;abc&quot;,&quot;car&quot;,&quot;ada&quot;,&quot;racecar&quot;,&quot;cool&quot;]
Output: &quot;ada&quot;
Explanation: The first string that is palindromic is &quot;ada&quot;.
Note that &quot;racecar&quot; is also palindromic, but it is not the first.
" data-snippet-id="ext.2bf6d91fce81fe285f1a045174921f27" data-snippet-saved="false" data-codota-status="done"><strong>Input:</strong> words = ["abc","car","ada","racecar","cool"]
<strong>Output:</strong> "ada"
<strong>Explanation:</strong> The first string that is palindromic is "ada".
Note that "racecar" is also palindromic, but it is not the first.
</pre>

<p><strong class="example">Example 2:</strong></p>

<div class="top-box hide"><div class="alert-info"></div></div><pre data-original-code="Input: words = [&quot;notapalindrome&quot;,&quot;racecar&quot;]
Output: &quot;racecar&quot;
Explanation: The first and only string that is palindromic is &quot;racecar&quot;.
" data-snippet-id="ext.b258a04d2b8886dfd843425a9d1f1f5b" data-snippet-saved="false" data-codota-status="done"><strong>Input:</strong> words = ["notapalindrome","racecar"]
<strong>Output:</strong> "racecar"
<strong>Explanation:</strong> The first and only string that is palindromic is "racecar".
</pre>

<p><strong class="example">Example 3:</strong></p>

<div class="top-box hide"><div class="alert-info"></div></div><pre data-original-code="Input: words = [&quot;def&quot;,&quot;ghi&quot;]
Output: &quot;&quot;
Explanation: There are no palindromic strings, so the empty string is returned.
" data-snippet-id="ext.cc3543920220417e54f40c2eda6449da" data-snippet-saved="false" data-codota-status="done"><strong>Input:</strong> words = ["def","ghi"]
<strong>Output:</strong> ""
<strong>Explanation:</strong> There are no palindromic strings, so the empty string is returned.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 100</code></li>
	<li><code>words[i]</code> consists only of lowercase English letters.</li>
</ul>
</div>