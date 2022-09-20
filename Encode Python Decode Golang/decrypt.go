package main

import (
	"crypto/rand"
	"crypto/rsa"
	"crypto/x509"
	"encoding/base64"
	"encoding/pem"
	"fmt"
	"os"
)

func keys() {

	// generate private key
	privatekey, err := rsa.GenerateKey(rand.Reader, 1024)

	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	var publickey *rsa.PublicKey
	publickey = &privatekey.PublicKey

	// save PEM file
	pemfile, err := os.Create("private.pem")

	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	var pemkey = &pem.Block{
		Type:  "RSA PRIVATE KEY",
		Bytes: x509.MarshalPKCS1PrivateKey(privatekey)}

	err = pem.Encode(pemfile, pemkey)

	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	pemfile2, err := os.Create("public.pem")

	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	var pemkey2 = &pem.Block{
		Type:  "RSA PUBLIC KEY",
		Bytes: x509.MarshalPKCS1PublicKey(publickey)}

	err = pem.Encode(pemfile2, pemkey2)

	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	pemfile.Close()

}

func decryptString(ct []byte) string {
	privateKey, _ := os.ReadFile("private.pem")
	block, _ := pem.Decode([]byte(privateKey))
	parsedKey, _ := x509.ParsePKCS1PrivateKey(block.Bytes)
	rng := rand.Reader
	plaintext, err := rsa.DecryptPKCS1v15(rng, parsedKey, ct)
	fmt.Println(err)
	fmt.Println("Plaintext:", string(plaintext))
	return string(plaintext)
}
func main() {
	// keys()     //Firstly generate the keys
	s := "mJm4OOwEnm+7bD5xJK/ErWYLwR9Z33mmF0j80cIZGxeTtK1w/UzOoI7paPklBJXBkhpWdiUIgA3uk3THZ8qxxkuoGM4Tv4+E+9f7cH+uSb0scGCbuysCjTW0hVNiwECMvRARgnfyxWvCCQ5ANsJANg4jrxnMLR+hvwNtI4hd+Gc="
	r, _ := base64.StdEncoding.DecodeString(s)
	fmt.Println("Here is encrypted text : ", decryptString(r))
}
