<h2><a href="https://leetcode.com/problems/reverse-words-in-a-string/">151. Reverse Words in a String</a></h2><h3>Medium</h3><hr><div><p>Given an input string <code>s</code>, reverse the order of the <strong>words</strong>.</p>

<p>A <strong>word</strong> is defined as a sequence of non-space characters. The <strong>words</strong> in <code>s</code> will be separated by at least one space.</p>

<p>Return <em>a string of the words in reverse order concatenated by a single space.</em></p>

<p><b>Note</b> that <code>s</code> may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="top-box hide"><div class="alert-info"></div></div><pre data-original-code="Input: s = &quot;the sky is blue&quot;
Output: &quot;blue is sky the&quot;
" data-snippet-id="ext.97ad4d2927fa4a277658337166984dc1" data-snippet-saved="false" data-codota-status="done"><strong>Input:</strong> s = "the sky is blue"
<strong>Output:</strong> "blue is sky the"
</pre>

<p><strong class="example">Example 2:</strong></p>

<div class="top-box hide"><div class="alert-info"></div></div><pre data-original-code="Input: s = &quot;  hello world  &quot;
Output: &quot;world hello&quot;
Explanation: Your reversed string should not contain leading or trailing spaces.
" data-snippet-id="ext.afafecccd786f5470e430967cfc64672" data-snippet-saved="false" data-codota-status="done"><strong>Input:</strong> s = "  hello world  "
<strong>Output:</strong> "world hello"
<strong>Explanation:</strong> Your reversed string should not contain leading or trailing spaces.
</pre>

<p><strong class="example">Example 3:</strong></p>

<div class="top-box hide"><div class="alert-info"></div></div><pre data-original-code="Input: s = &quot;a good   example&quot;
Output: &quot;example good a&quot;
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
" data-snippet-id="ext.a63bb8b79b47d91ba0b2e5cb7ca894f7" data-snippet-saved="false" data-codota-status="done"><strong>Input:</strong> s = "a good   example"
<strong>Output:</strong> "example good a"
<strong>Explanation:</strong> You need to reduce multiple spaces between two words to a single space in the reversed string.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> contains English letters (upper-case and lower-case), digits, and spaces <code>' '</code>.</li>
	<li>There is <strong>at least one</strong> word in <code>s</code>.</li>
</ul>

<p>&nbsp;</p>
<p><b data-stringify-type="bold">Follow-up:&nbsp;</b>If the string data type is mutable in your language, can&nbsp;you solve it&nbsp;<b data-stringify-type="bold">in-place</b>&nbsp;with&nbsp;<code data-stringify-type="code">O(1)</code>&nbsp;extra space?</p>
</div>