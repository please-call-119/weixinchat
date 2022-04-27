<!-- wp:paragraph {"fontSize":"medium"} -->
<p class="has-medium-font-size"><strong>简介：</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>自动转发微信的消息，也可以用作微信消息发送来使用，可考虑后续结合同花顺自动交易模块来实现交易信息及时通知，目前还未结合，待后续有时间更新</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>思路：</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>使用pywinauto模块（其实国内也有类似的库，叫<a href="https://github.com/yinkaisheng/Python-UIAutomation-for-Windows"><strong>uiautomation</strong></a>，我测试下来感觉更高效，但是没有什么资料）操作句柄，<strong><span class="has-inline-color has-luminous-vivid-orange-color">如要转载请标明来源</span></strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>工具：</strong></p>
<!-- /wp:paragraph -->

<!-- wp:preformatted -->
<pre id="block-687cf51d-5fa4-4ae8-ae2e-063b6e16f850" class="wp-block-preformatted">pycharm
anaconda（虽然有些臃肿，但是我们并不是要成为专业开发者，一切以便利和可复用为导向</pre>
<!-- /wp:preformatted -->

<!-- wp:paragraph -->
<p><strong>环境：</strong></p>
<!-- /wp:paragraph -->

<!-- wp:preformatted -->
<pre id="block-0d62f4de-9663-411b-88f1-1d5ef42eb1a7" class="wp-block-preformatted">Python3.9.7
pywin32-300（最新版本应该是302，但是会出现找不到模块的错误，最好更换成300或者之前的版本）
pywinauto0.6.8 </pre>
<!-- /wp:preformatted -->

<!-- wp:paragraph -->
<p><strong>环境安装：</strong>（如果不会使用anaconda控制台，建议先百度教程看看，后续我也会写anaconda一些简单操作）</p>
<!-- /wp:paragraph -->

<!-- wp:preformatted -->
<pre id="block-2146a025-5c8e-4c9a-95bd-0c9800bf99d0" class="wp-block-preformatted">conda环境安装：
pip install --upgrade pywin32==300 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install pywinauto -i https://pypi.tuna.tsinghua.edu.cn/simple</pre>
<!-- /wp:preformatted -->
