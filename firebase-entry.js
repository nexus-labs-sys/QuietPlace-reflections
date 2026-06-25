import { initializeApp } from "firebase/app";

import {
  getAuth,
  onAuthStateChanged,
  signInWithEmailAndPassword,
  createUserWithEmailAndPassword,
  signInWithPopup,
  signInWithRedirect,
  getRedirectResult,
  sendPasswordResetEmail,
  signInWithCustomToken,
  GoogleAuthProvider,
  updateProfile,
  signOut
} from "firebase/auth";

import {
  getFirestore,
  doc,
  getDoc,
  setDoc,
  deleteDoc
} from "firebase/firestore";

window.FirebaseBundle = {
  initializeApp,

  getAuth,
  onAuthStateChanged,
  signInWithEmailAndPassword,
  createUserWithEmailAndPassword,
  signInWithPopup,
  signInWithRedirect,
  getRedirectResult,
  sendPasswordResetEmail,
  signInWithCustomToken,
  GoogleAuthProvider,
  updateProfile,
  signOut,

  getFirestore,
  doc,
  getDoc,
  setDoc,
  deleteDoc
};