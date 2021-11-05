with import <nixpkgs> {};
stdenv.mkDerivation {
  name = "python-mysql-practice";
  buildInputs = ( with pkgs; [
    mysql80
    black
  ]) ++ ( with pkgs.python39Packages; [
    mysql-connector
  ]);
}
