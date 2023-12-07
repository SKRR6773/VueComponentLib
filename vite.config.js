import { fileURLToPath, URL } from 'node:url'
import { run } from 'vite-plugin-run'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    run([
      {
        name: "watch dog",
        run: [
          "api/Scripts/python.exe", "api/write.py"
        ],
        onFileChanged: function(a)
        {
          console.log("Hello 'World!");
        }
      }
    ]),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
