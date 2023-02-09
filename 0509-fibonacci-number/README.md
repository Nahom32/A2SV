<h2><a href="https://leetcode.com/problems/fibonacci-number/">509. Fibonacci Number</a></h2><h3>Easy</h3><hr><div><p>The <b>Fibonacci numbers</b>, commonly denoted <code>F(n)</code> form a sequence, called the <b>Fibonacci sequence</b>, such that each number is the sum of the two preceding ones, starting from <code>0</code> and <code>1</code>. That is,</p>

<div class="top-box hide"><div class="alert-info"></div></div><pre data-original-code="F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
" data-snippet-id="ext.00b27ec44f04b7065c2a1b4dded3461b" data-snippet-saved="false" data-codota-status="done">F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n &gt; 1.
</pre>

<p>Given <code>n</code>, calculate <code>F(n)</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="top-box hide"><div class="alert-info"></div></div><pre data-original-code="Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
" data-snippet-id="ext.3a4332f38e1c8e023c12a128c82c6c72" data-snippet-saved="false" data-codota-status="done"><strong>Input:</strong> n = 2
<strong>Output:</strong> 1
<strong>Explanation:</strong> F(2) = F(1) + F(0) = 1 + 0 = 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<div class="top-box hide"><div class="alert-info"></div></div><pre data-original-code="Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
" data-snippet-id="ext.dc7906cdfe006809d963f1fcb3dadc08" data-snippet-saved="false" data-codota-status="done"><strong>Input:</strong> n = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> F(3) = F(2) + F(1) = 1 + 1 = 2.
</pre>

<p><strong class="example">Example 3:</strong></p>

<div class="top-box hide"><div class="alert-info"></div></div><pre data-original-code="Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
" data-snippet-id="ext.3740bf06e41ad423e6d646d805c7e08c" data-snippet-saved="false" data-codota-status="done"><strong>Input:</strong> n = 4
<strong>Output:</strong> 3
<strong>Explanation:</strong> F(4) = F(3) + F(2) = 2 + 1 = 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 30</code></li>
</ul>
</div>