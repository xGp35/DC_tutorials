### Make Firefox fast again

Two ways:

**Method 1:**

- Go to `about:restartrequired` and choose to restart Firefox, restoring all tabs (*this is the same restart prompt that appears after Firefox has been updated*).

**Method 2:** (see **warning** below)

1. Go to `about:processes`, sort by the memory column (*largest 1st*), then click the "X" on the right to close the largest memory-usage webpages (*often YouTube, which may appear several times*).
2. Then go to `about:memory` and under "Free memory," choose:

   - `GC` (*global garbage collection*)
   - `CC` (*cycle collection*)
   - `minimize memory usage*

**Method 3:**  
I said two methods, but there's also `about:unloads` that I just remembered, but I don't remember how it works. I'm going to revisit that one.

---

Please heed this warning:

**WARNING:** Be careful using Method 2 because it **will not prompt you** if you have unsubmitted entries in tabs (like a Reddit comment) like the first method would. You would just ***lose your work***.

---

I used to use the first method, but I switched to the second method because the first resets anything temporarily enabled.

(*Example of temporarily-enabled things: (1) the element zapper in uBlock Origin (lightning bolt), but in my case, it's usually for (2) NoScript—an advanced tool that blocks all scripts except the ones from sources you explicitly allow—for which any temporarily enabled scripts would be reset with the 1st method.*)

---

Again, this is something I (*me, personally, this person right here, not you*) do if I have unfinished work in many tabs (200 to 500 in my case), but have opened 100 YouTube tabs that wind up using a *LOT* of memory. I do this to clear that memory. Reopening the browser after the 'method 1' restart causes any tabs to not be activated until visited again.

This might not be for you, and that's OK. But it may help someone who needs to keep many tabs open at once.

Yes, I expect comments about how I wind up using many tabs, why I would, etc.. why not this, or this.. and I welcome them all, but please keep in mind that this may be helpful for the people that need it. Thank you.

And if you're truly curious how and why I use so many tabs, those answers are:

- [here](https://old.reddit.com/r/firefox/comments/17k0a6g/is_it_possible_to_manually_refresh_firefox_the/k79wxvj/)
- and [here](https://old.reddit.com/r/firefox/comments/17k0a6g/is_it_possible_to_manually_refresh_firefox_the/k79p3sw/)

---

<sup>keywords: firefox slow, lots of tabs, low memory, so much memory, slowing firefox down, optimize Firefox, refresh Firefox, sessions</sup>

I hope this helps someone now or in the future.
