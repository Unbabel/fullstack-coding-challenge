// postcss.config.js
const tailwindcss = require('tailwindcss');

module.exports = {
  plugins: [
    tailwindcss('./tailwind.js'),
    require('autoprefixer'),
    require('@fullhuman/postcss-purgecss')({
      content: ['./src/**/*.jsx', './src/**/*.js', './public/index.html'],
      css: ['./src/assets/styles/tailwind.css'],
      // Include any special characters you're using in this regular expression
      defaultExtractor: content => content.match(/[A-Za-z0-9-_:/]+/g) || [],
    }),
  ],
};
