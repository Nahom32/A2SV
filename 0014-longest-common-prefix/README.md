<h2><a href="https://leetcode.com/problems/longest-common-prefix/">14. Longest Common Prefix</a></h2><h3>Easy</h3><hr><div><p>Write a function to find the longest common prefix string amongst an array of strings.</p>

<p>If there is no common prefix, return an empty string <code>""</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="top-box hide"><div class="alert-info"></div></div><div class="top-box hide"><div class="alert-info"></div></div><pre data-original-code="Input: strs = [&quot;flower&quot;,&quot;flow&quot;,&quot;flight&quot;]
Output: &quot;fl&quot;
" data-snippet-id="ext.11565f075cb45b1e83e1c94b5f3ea86d" data-snippet-saved="false" data-codota-status="done"><strong>Input:</strong> strs = ["flower","flow","flight"]
<strong>Output:</strong> "fl"
</pre>

<p><strong class="example">Example 2:</strong></p>

<div class="top-box hide"><div class="alert-info"></div></div><div class="top-box hide"><div class="alert-info"></div></div><pre data-original-code="Input: strs = [&quot;dog&quot;,&quot;racecar&quot;,&quot;car&quot;]
Output: &quot;&quot;
Explanation: There is no common prefix among the input strings.
" data-snippet-id="ext.3c5df5a80526811b6a89acfbfdd4856e" data-snippet-saved="false" data-codota-status="done"><strong>Input:</strong> strs = ["dog","racecar","car"]
<strong>Output:</strong> ""
<strong>Explanation:</strong> There is no common prefix among the input strings.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= strs.length &lt;= 200</code></li>
	<li><code>0 &lt;= strs[i].length &lt;= 200</code></li>
	<li><code>strs[i]</code> consists of only lowercase English letters.</li>
</ul>
</div>