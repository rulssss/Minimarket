// Configuración de Firebase para Next.js
import { initializeApp, getApps } from "firebase/app";
import { getAuth } from "firebase/auth";
import { getFirestore } from "firebase/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyAwEpdM7SjHYfvo4OBDU8fqaTmbe5fVNMs",
  authDomain: "rlsweb-c10d9.firebaseapp.com",
  projectId: "rlsweb-c10d9",
  storageBucket: "rlsweb-c10d9.appspot.com", // corregido: ".app" ➝ ".appspot.com"
  messagingSenderId: "133024126169",
  appId: "1:133024126169:web:0ae7ef990feec829d41ac8",
  measurementId: "G-0PS28W27NW"
};

const app = !getApps().length ? initializeApp(firebaseConfig) : getApps()[0];
const auth = getAuth(app);
const db = getFirestore(app);

export { auth, db };