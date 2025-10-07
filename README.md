
<h2 class="wp-block-heading">前書き</h2>



<p>このリポジトリは、xargsコマンドを実行して他のコマンドが出力した文字列を整形する体験ができます</p>



<h2 class="wp-block-heading">インストールする必要のあるコマンド</h2>



<ol class="wp-block-list">
<li>git</li>
</ol>



<h2 class="wp-block-heading">クイックスタート</h2>



<p>上記のコマンドをインストール済みの方は、以下のコマンドを実行してリポジトリからダウンロード後、ディレクトリを移動し、xargsコマンドを実行して出力結果が変化することを確認してください</p>



<h3 class="wp-block-heading">ubuntu</h3>



<pre class="wp-block-code has-24292-eff-color has-cyan-bluish-gray-background-color has-text-color has-background has-1-125-rem-font-size"><code>git clone https://github.com/trygfmi/xargs_shapeString
cd xargs_shapeString
find . -type f -name "*.txt"
find . -type f -name "*.txt" | xargs</code></pre>



<h3 class="wp-block-heading">macos</h3>



<p>※MacPortsを使用しています</p>



<pre class="wp-block-code has-24292-eff-color has-cyan-bluish-gray-background-color has-text-color has-background has-1-125-rem-font-size"><code>git clone https://github.com/trygfmi/xargs_shapeString
cd xargs_shapeString
find . -type f -name "*.txt"
find . -type f -name "*.txt" | xargs</code></pre>



<h3 class="wp-block-heading">windows</h3>



<p>※MSYS2 MINGW64を使用しています</p>



<pre class="wp-block-code has-24292-eff-color has-cyan-bluish-gray-background-color has-text-color has-background has-1-125-rem-font-size"><code>git clone https://github.com/trygfmi/xargs_shapeString
cd xargs_shapeString
find . -type f -name "*.txt"
find . -type f -name "*.txt" | xargs</code></pre>



<h2 class="wp-block-heading">実行手順</h2>



<h3 class="wp-block-heading">ubuntu</h3>



<details class="wp-block-details"><summary>クリックして詳細を開く</summary>
<h4 class="wp-block-heading">事前確認</h4>



<p>以下のコマンドを端末に打ち込んでcommand not foundが出なければokです</p>



<pre class="wp-block-code has-24292-eff-color has-cyan-bluish-gray-background-color has-text-color has-background has-1-125-rem-font-size"><code>git --version</code></pre>



<h4 class="wp-block-heading">preinstall</h4>



<p>command not foundが出たコマンドを以下のコマンドでインストールしてください</p>



<pre class="wp-block-code has-24292-eff-color has-cyan-bluish-gray-background-color has-text-color has-background has-1-125-rem-font-size"><code>sudo apt install git</code></pre>



<h4 class="wp-block-heading">コマンド</h4>



<p>以下のコマンドを実行することで詳細のような文字列が出力されるはずです</p>



<pre class="wp-block-code has-24292-eff-color has-cyan-bluish-gray-background-color has-text-color has-background has-1-125-rem-font-size"><code>git clone https://github.com/trygfmi/xargs_shapeString
cd xargs_shapeString
find . -type f -name "*.txt"
find . -type f -name "*.txt" | xargs</code></pre>



<details class="wp-block-details"><summary>詳細</summary>
<p class="has-24292-eff-color has-cyan-bluish-gray-background-color has-text-color has-background has-1-125-rem-font-size">./folder1/example3.txt<br>./folder1/example2.txt<br>./folder1/folder2/example4.txt<br>./folder1/folder3/example5.txt<br>./example1.txt<br><br>./folder1/example3.txt ./folder1/example2.txt ./folder1/folder2/example4.txt ./folder1/folder3/example5.txt ./example1.txt</p>
</details>
</details>



<h3 class="wp-block-heading">macos</h3>



<details class="wp-block-details"><summary>クリックして詳細を開く</summary>
<h4 class="wp-block-heading">事前確認</h4>



<p>以下のコマンドをターミナルに打ち込んでcommand not foundが出なければokです</p>



<pre class="wp-block-code has-24292-eff-color has-cyan-bluish-gray-background-color has-text-color has-background has-1-125-rem-font-size"><code>source ~/bashrc_folder/macports_alias
git --version</code></pre>



<p>※macosはMacPortsパッケージマネージャを使用してコマンドを管理します。もしインストールしていない方は以下のリンクからMacPortsのインストール手順をご覧ください</p>



<p>またコマンドに別名を設定して既存の環境と競合しないでコマンドを呼び出せるようにします。</p>



<p>初めてこのブログを利用する方は、以下の2つの記事を参考に環境構築してください</p>



[![MacPortsをインストールするまでの手順](https://ss523971.stars.ne.jp/todo/wp-content/uploads/2025/10/thumbnail_macports_title_1920_1080_2.png,)](https://ss523971.stars.ne.jp/todo/2025/10/02/macports%e3%82%92%e3%82%a4%e3%83%b3%e3%82%b9%e3%83%88%e3%83%bc%e3%83%ab%e3%81%99%e3%82%8b%e3%81%be%e3%81%a7%e3%81%ae%e6%89%8b%e9%a0%86/)



[![MacPortsでインストールしたコマンドのエイリアス設定](https://ss523971.stars.ne.jp/todo/wp-content/uploads/2025/10/thumbnail_macports2.png,)](https://ss523971.stars.ne.jp/todo/2025/10/03/macports%e3%81%a7%e3%82%a4%e3%83%b3%e3%82%b9%e3%83%88%e3%83%bc%e3%83%ab%e3%81%97%e3%81%9f%e3%82%b3%e3%83%9e%e3%83%b3%e3%83%89%e3%81%ae%e3%82%a8%e3%82%a4%e3%83%aa%e3%82%a2%e3%82%b9%e8%a8%ad%e5%ae%9a/)



<h4 class="wp-block-heading">preinstall</h4>



<p>command not foundが出たコマンドを以下のコマンドでインストールしてエイリアスを設定してください</p>



<pre class="wp-block-code has-24292-eff-color has-cyan-bluish-gray-background-color has-text-color has-background has-1-125-rem-font-size"><code>sudo port install git
echo 'alias git="/opt/local/bin/git"' &gt;&gt; ~/bashrc_folder/macports_alias</code></pre>



<h4 class="wp-block-heading">コマンド</h4>



<p>以下のコマンドを実行することで詳細のような文字列が出力されるはずです</p>



<pre class="wp-block-code has-24292-eff-color has-cyan-bluish-gray-background-color has-text-color has-background has-1-125-rem-font-size"><code>source ~/bashrc_folder/macports_alias
git clone https://github.com/trygfmi/xargs_shapeString
cd xargs_shapeString
find . -type f -name "*.txt"
find . -type f -name "*.txt" | xargs</code></pre>



<details class="wp-block-details"><summary>詳細</summary>
<p class="has-24292-eff-color has-cyan-bluish-gray-background-color has-text-color has-background has-1-125-rem-font-size">./example1.txt<br>./folder1/example2.txt<br>./folder1/example3.txt<br>./folder1/folder2/example4.txt<br>./folder1/folder3/example5.txt<br><br>./example1.txt ./folder1/example2.txt ./folder1/example3.txt ./folder1/folder2/example4.txt ./folder1/folder3/example5.txt</p>
</details>
</details>



<h3 class="wp-block-heading">windows</h3>



<details class="wp-block-details"><summary>クリックして詳細を開く</summary>
<h4 class="wp-block-heading">事前確認</h4>



<p>以下のコマンドをMSYS2 MINGW64に打ち込んでcommand not foundが出なければokです</p>



<pre class="wp-block-code has-24292-eff-color has-cyan-bluish-gray-background-color has-text-color has-background has-1-125-rem-font-size"><code>git --version</code></pre>



<p>※windowsはMSYS2 MINGW64で確認しています。もしインストールしていない方は以下のリンクからmsys2のインストール手順をご覧ください</p>



[![[windows] msys2をインストールするまでの手順](https://ss523971.stars.ne.jp/todo/wp-content/uploads/2025/10/msys2_thumbnail_1920_1080.png)](https://ss523971.stars.ne.jp/todo/2025/10/02/windows-msys2%e3%82%92%e3%82%a4%e3%83%b3%e3%82%b9%e3%83%88%e3%83%bc%e3%83%ab%e3%81%99%e3%82%8b%e3%81%be%e3%81%a7%e3%81%ae%e6%89%8b%e9%a0%86/)



<h4 class="wp-block-heading"><strong>preinstall</strong></h4>



<p>command not foundが出たコマンドを以下のコマンドでインストールしてください</p>



<pre class="wp-block-code has-24292-eff-color has-cyan-bluish-gray-background-color has-text-color has-background has-1-125-rem-font-size"><code>pacman --sync git</code></pre>



<h4 class="wp-block-heading"><strong>コマンド</strong></h4>



<p>以下のコマンドを実行することで詳細のような文字列が出力されるはずです</p>



<pre class="wp-block-code has-24292-eff-color has-cyan-bluish-gray-background-color has-text-color has-background has-1-125-rem-font-size"><code>git clone https://github.com/trygfmi/xargs_shapeString
cd xargs_shapeString
find . -type f -name "*.txt"
find . -type f -name "*.txt" | xargs</code></pre>



<details class="wp-block-details"><summary>詳細</summary>
<p class="has-24292-eff-color has-cyan-bluish-gray-background-color has-text-color has-background has-1-125-rem-font-size">./example1.txt<br>./folder1/example2.txt<br>./folder1/example3.txt<br>./folder1/folder2/example4.txt<br>./folder1/folder3/example5.txt<br><br>./example1.txt ./folder1/example2.txt ./folder1/example3.txt ./folder1/folder2/example4.txt ./folder1/folder3/example5.txt</p>
</details>
</details>



<h2 class="wp-block-heading">後書き</h2>



<p>複数行を空白区切りで一つの行に出力するのが特徴です</p>



<h2 class="wp-block-heading">この記事で使用したコマンドで実行できるお薦め記事</h2>



<h2 class="wp-block-heading">この記事で使用しているキーボード</h2>



<p></p>



<p></p>
