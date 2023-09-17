# codetop

<https://codetop.yusanshi.com/>

A wrapper website for reviewing and tracking problems at <https://codetop.cc/>.

![image](https://github.com/yusanshi/codetop/assets/36265606/e5ac323f-e137-431a-9563-d8da8c901c93)


## Tracking status locally

If you visit <https://codetop.yusanshi.com/> directly, the status will be tracked locally with [localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage).

## Tracking status remotely

By using a remote storage server, you can sync your status across different devices:

1. Create an account at <https://vercel.com/>. Go to <https://vercel.com/dashboard/stores> and create a KV database (the free plan is enough).

2. Copy `endpoint` and `bearer` as shown below:
![image](https://github.com/yusanshi/codetop/assets/36265606/62cd7610-5938-45cb-8e57-c9d523441167)

3. Go to `https://codetop.yusanshi.com/?endpoint={endpoint}&bearer={bearer}` (replace `{endpoint}` and `{bearer}` with the corresponding values).

   > Note: if the `bearer` value contain `+`, `/` or `=`, you should encode it with [URL encoding](https://en.wikipedia.org/wiki/Percent-encoding):
   >
   > ```
   > +: %2B
   > /: %2F
   > =: %3D
   > ```
   > For example, if `bearer` is `ABCDEFG==`,  then your target URL is `...&bearer=ABCDEFG%3D%3D`.
